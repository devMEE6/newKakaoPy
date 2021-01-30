from .BasePacket import PacketReq, PacketRes

class PingPacketReq(PacketReq):
    def __init__(self, packet_name, body):
        super().__init__("PING", body)
        self.packet_name = "PING"
        self.body = {}
        
class PacketPingRes(PacketRes):
    def __init__(self, packet):
        super().__init__(packet)
        self.packet_name = "PING"
        
        self.status = packet["Body"]["status"]
