import socket

from .Config import Agent, NetType, Version, MCCMNC, Lang
from .Utils import cryptoUtils
from .Utils import packetUtils


def getCheckInData(host, port):
    sock = socket.socket()
    sock.connect((host, port))
    
    aes_key = cryptoUtils.getRandomAesKey()
    
    sock.send(cryptoUtils.getHandshakePacket(aes_key))
    
    checkInPacket = packetUtils.toLocoPacket(1000, "CHECKIN", {
        "userId": 0,
        "os": Agent,
        "ntype": NetType,
        "appVer": Version,
        "MCCMNC": MCCMNC,
        "lang": Lang,
    })

    sock.send(cryptoUtils.encryptPacket(checkInPacket, aes_key))

    recv_packet = sock.recv(2048)
    
    decrypted_packet = cryptoUtils.decryptPacket(recv_packet, aes_key)
    
    result = packetUtils.readLocoPacket(decrypted_packet)

    return result["Body"]
