from .BasePacket import PacketRes
from ..Utils import messageUtils

class MsgPacketRes(PacketRes):
    def __init__(self, packet):
        super().__init__(packet)
        self.packet_name = "MSG"
        
        self.data = messageUtils.getMessageData(packet["Body"])
        
    def __getattr__(self, name):
        return self.data[name]
