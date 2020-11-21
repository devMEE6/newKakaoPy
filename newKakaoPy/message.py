from .Utils import messageUtils
from .Packets.WritePacket import WritePacketReq

class message():
    def __init__(self, sendPacket, packet):
        self.data = messageUtils.getMessageData(packet["Body"])
        self.sendPacket = sendPacket
        
    def __getattr__(self, name):
        return self.data[name]
        
    async def sendChat(self, chat):
        return await self.sendPacket(WritePacketReq(self.data["chatId"],  chat.getAttachment(), chat.getType(), 1, chat.getMessage()))
