from .BasePacket import PacketRes

class MsgPacketRes(PacketRes):
    def __init__(self, packet):
        self.packet_name = "MSG"
        
        self.chatId = packet["Body"]["chatLog"]["chatId"]
        self.msgId = packet["Body"]["chatLog"]["msgId"]
        self.logId = packet["Body"]["chatLog"]["logId"]
        self.prevId = packet["Body"]["chatLog"]["prevId"]
        self.sendAt = packet["Body"]["chatLog"]["sendAt"]
        self.type = packet["Body"]["chatLog"]["type"]
        self.senderId = packet["Body"]["chatLog"]["authorId"]
        self.senderName = packet["Body"]["authorNickname"]
        self.message = packet["Body"]["chatLog"]["message"]
        
        if "attachment" in packet["Body"]["chatLog"]:
            if packet["Body"]["chatLog"]["attachment"] != "":
                self.attachment = {}
            else:
                self.attachment = packet["Body"]["chatLog"]["attachment"]
        else:
            self.attachment = {}
