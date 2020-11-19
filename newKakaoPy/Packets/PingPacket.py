from .BasePacket import PacketReq, PacketRes

class PingPacketReq(PacketReq):
    def __init__(self):
        self.packet_name = "PING"
        self.body = {}
        
class PacketPingRes(PacketRes):
    def __init__(self, packet):
        self.packet_name = "PING"
        
        self.status = packet["Body"]["status"]
