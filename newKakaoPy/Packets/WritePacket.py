from .BasePacket import PacketReq, PacketRes

class WritePacketReq(PacketReq):
    def __init__(self, chatId, extra, type, msgId, msg, noSeen):
        self.packet_name = "WRITE"
        
        self.body = {
            "chatId": chatId,
            "extra": str(extra),
            "type": type,
            "msgId": msgId,
            "msg": msg,
            "noSeen": noSeen
        }
        
class WritePacketRes(PacketRes):
    def __init__(self, packet):
        self.packet_name = "WRITE"
        
        self.chatId = packet["Body"]["chatId"]
        self.msgId = packet["Body"]["msgId"]
        self.logId = packet["Body"]["logId"]
        self.prevId = packet["Body"]["prevId"]
        self.sendAt = packet["Body"]["sendAt"]
