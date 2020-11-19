from .cryptoManager import CryptoManager
from .Utils import packetUtils

import io
import bson
import struct
import socket

def getCheckInData(host, port):
    crypto = CryptoManager()

    sock = socket.socket()
    sock.connect((host, port))

    handshakePacket = crypto.getHandshakePacket()
    sock.send(handshakePacket)
    
    packet = packetUtils.toLocoPacket(1000, "CHECKIN", {
        "userId": 0,
        "os": "win32",
        "ntype": 0,
        "appVer": "3.14",
        "MCCMNC": "999",
        "lang": "ko",
    })

    sock.send(crypto.encryptPacket(packet))

    data = sock.recv(2048)
    
    data = crypto.decryptPacket(data)
    
    result = packetUtils.readLocoPacket(data)

    return result["Body"]
