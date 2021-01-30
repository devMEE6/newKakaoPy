from .BasePacket import PacketReq, PacketRes

class LoginListPacketReq(PacketReq):
    def __init__(self, duuid, oauthToken, packet_name, body):
        super().__init__(packet_name, body)
        self.packet_name = "LOGINLIST"
        
        self.body = {
            "appVer": "3.1.4",
            "prtVer": "1",
            "os": "win32",
            "lang": "ko",
            "duuid": duuid,
            "oauthToken": oauthToken,
            "dtype": 2,
            "ntype": 999,
            "MCCMNC": "999",
            "revision": 0,
            "chatIds": [],
            "maxIds": [],
            "lastTokenId": 0,
            "lbk": 0,
            "bg": False,
        }
        
class LoginListPacketRes(PacketRes):
    def __init__(self, packet):
        self.packet_name = "LOGINLIST"
