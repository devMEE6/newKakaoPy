class PacketReq:
    def __init__(self, packet_name, body):
        self.packet_name = packet_name
        self.body = body

    def getPacketName(self):
        return self.packet_name

    def getBody(self):
        return self.body

class PacketRes:
    def __init__(self, packet):
        self.packet_name = packet["PacketName"]
        self.body = packet["Body"]
        
    def getPacketName(self):
        return self.packet_name
