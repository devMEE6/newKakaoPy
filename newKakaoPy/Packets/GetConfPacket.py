from .BasePacket import PacketReq, PacketRes

class PacketGetconfReq(PacketReq):
    def __init__(self, os, model, MCCMNC, packet_name, body):
        super().__init__("GETCONF", body)
        self.packet_name = "GETCONF"
        self.body = {
            "os":os,
            "model":model,
            "MCCMNC":MCCMNC
        }
        
class PacketGetconfRes(PacketRes):
    def __init__(self, packet):
        super().__init__(packet)
        self.packet_name = "GETCONF"
        
        self.status = packet["Body"]["status"]
        self.revision = packet["Body"]["revision"]
        self.info3g = packet["Body"]["3g"]
        self.infoWifi = packet["Body"]["wifi"]
        self.ticket = packet["Body"]["ticket"]
        self.profile = packet["Body"]["profile"]
        self.etc = packet["Body"]["etc"]
        self.trailer = packet["Body"]["trailer"]
        self.trailer_h = packet["Body"]["trailer.h"]
