from .Utils import packetUtils
from .Utils import cryptoUtils
from .Packets.PingPacket import PingPacketReq
from .Packets.LoginListPacket import LoginListPacketReq

import os
import socket
import asyncio
import struct

class LocoClient():
    def __init__(self):
        self.receiver = {}
        
        self.reader = None
        self.writer = None
        
        self.packet_id = 0
        self.packet_dict = {}
        
        self.access_token = ""
        self.device_uuid = ""
        self.aes_key = b""
        
        self.processing_buf = b""
        self.processing_size = -1
        
    async def sendPacket(self, packet):
        self.packet_id += 1
        
        loco_packet = cryptoUtils.encryptPacket(packetUtils.toLocoPacket(self.packet_id, packet.packet_name, packet.getBody()), self.aes_key)
        
        self.writer.write(loco_packet)
        await self.writer.drain()
        
        future = asyncio.get_event_loop().create_future()
        self.packet_dict[self.packet_id] = future
        
        return future
    
    async def recvPacket(self):
        print("recv")
        readBuffer = b""
        packetSize = -1

        while True:
            recv = await self.reader.read(512)
            readBuffer += recv

            if packetSize == -1 and len(readBuffer) >= 4:
                packetSize = struct.unpack("<I", readBuffer[0:4])[0] + 4
            if packetSize != -1:
                if len(readBuffer) >= packetSize:
                    await self.processPacket(readBuffer[4:packetSize])
                    readBuffer = readBuffer[packetSize:]
                    packetSize = -1
                    
    async def processPacket(self, packet):
        data = packet[16:]
        iv = packet[:16]
        
        self.processing_buf += cryptoUtils.aesDecrypt(data, self.aes_key, iv)
        if self.processing_size == -1 and len(self.processing_buf) >= 22:
            self.processing_size = struct.unpack("<I", self.processing_buf[18:22])[0] + 22
        if self.processing_size != -1 and len(self.processing_buf) >= self.processing_size:
            asyncio.get_event_loop().create_task(self.handlePacket(self.processing_buf[:self.processing_size]))
            
            self.processing_buf = self.processing_buf[self.processing_size:]
            self.processing_size = -1
            
    async def handlePacket(self, packet):
        #TODO 패킷 핸들러 호출 최적화
        packet = packetUtils.readLocoPacket(packet)
        loop = asyncio.get_event_loop()
        
        if packet["PacketID"] in self.packet_dict:
            self.packet_dict[packet["PacketID"]].set_result(packet["Body"])
            del self.packet_dict[packet["PacketID"]]
            
        if packet["PacketName"] in self.receiver:
            for i in self.receiver[packet["PacketName"]]:
                if i["packet_class"]:
                    loop.create_task(i["handler"](i["packet_class"](packet)))
                else:
                    loop.create_task(i["handler"](packet))
                
        if "ALL" in self.receiver:
            for i in self.receiver["ALL"]:
                if i["packet_class"]:
                    loop.create_task(i["handler"](i["packet_class"](packet)))
                else:
                    loop.create_task(i["handler"](packet))
                
    async def heartbeat(self):
        #TODO 연결 해제에 관한 heartbeat 처리
        while True:
            try:
                await asyncio.sleep(180)
                self.sendPacket(PingPacketReq())
            except:
                break
            
    async def start(self, receiver, server_ip, server_port, device_uuid, access_token):
        self.processing_buf = b""
        self.processing_size = -1
        
        self.access_token = access_token
        self.device_uuid = device_uuid
        
        self.receiver = receiver
        
        loop = asyncio.get_event_loop()
        
        while True:
            self.reader, self.writer = await asyncio.open_connection(server_ip, server_port)
            self.aes_key = os.urandom(16)
        
            self.writer.write(cryptoUtils.getHandshakePacket(self.aes_key))
            await self.writer.drain()
            
            loop.create_task(self.sendPacket(LoginListPacketReq(device_uuid, access_token)))
            loop.create_task(self.heartbeat())
            
            await self.recvPacket()
            print("Disconnected")
