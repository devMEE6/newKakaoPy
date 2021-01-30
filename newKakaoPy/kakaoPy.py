from .locoClient import LocoClient
from . import httpApi
from . import booking
from . import checkIn

import json
import asyncio

class kakaoPy():
    def __init__(self, uid, upw, device_name, device_uuid):
        self.handlers = {"message":[], "packet":{}}
        
        self.user_id = uid
        self.user_pw = upw
        self.device_name = device_name
        self.device_uuid = device_uuid
        self.locoClient = None
        
    #TODO None로 체크하는게 좋을지 receiveWithClass(?) 같은 함수를 따로 만드는게 좋을지..
    def packetReceive(self, packet_name, packet_class = None):
        def decorator(handler):
            if packet_name not in self.handlers["packet"]:
                self.handlers["packet"][packet_name] = []
            self.handlers["packet"][packet_name].append({"handler":handler, "packet_class":packet_class})
        return decorator
        
    def messageReceive(self):
        def decorator(handler):
            self.handlers["message"].append({"handler":handler})
        return decorator
        
    async def sendPacket(self, packet):
        return await self.locoClient.sendPacket(packet)
    
    def run(self):
        bookingData = booking.getBookingData()
        checkInData = checkIn.getCheckInData(bookingData["ticket"]["lsl"][0], bookingData["wifi"]["ports"][0])
            
        self.locoClient = LocoClient()
        result = json.loads(httpApi.Login(self.user_id, self.user_pw, self.device_name, self.device_uuid))
        if result["status"] != 0:
            print(result["status"], result["message"])
            return
        asyncio.get_event_loop().run_until_complete(self.locoClient.start(self.handlers, checkInData["host"], checkInData["port"], self.device_uuid, result["access_token"]))
