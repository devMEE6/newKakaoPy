from .Utils import cryptoUtils
from .Utils import packetUtils

import socket

def getCheckInData(host, port):
    sock = socket.socket()
    sock.connect((host, port))
    
    aes_key = cryptoUtils.getRandomAesKey()
    
    sock.send(cryptoUtils.getHandshakePacket(aes_key))
    
    checkInPacket = packetUtils.toLocoPacket(1000, "CHECKIN", {
        "userId": 0,
        "os": "win32",
        "ntype": 0,
        "appVer": "3.14",
        "MCCMNC": "999",
        "lang": "ko",
    })

    sock.send(cryptoUtils.encryptPacket(checkInPacket, aes_key))

    recv_packet = sock.recv(2048)
    
    decrypted_packet = cryptoUtils.decryptPacket(recv_packet, aes_key)
    
    result = packetUtils.readLocoPacket(decrypted_packet)

    return result["Body"]
