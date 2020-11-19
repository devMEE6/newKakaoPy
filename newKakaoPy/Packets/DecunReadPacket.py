from .BasePacket import PacketRes
        
class PacketDecunReadRes(PacketRes):
    def __init__(self, packet):
        self.packet_name = "DECUNREAD"
        
        self.status = packet["Body"]["status"]
        self.chatId = packet["Body"]["chatId"]
        self.userId = packet["Body"]["userId"]
        self.watermark = packet["Body"]["watermark"]
