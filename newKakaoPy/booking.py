from .Utils import packetUtils

import socket
import ssl
import bson

def getBookingData():
    hostname = 'booking-loco.kakao.com'
    context = ssl.create_default_context()

    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            packet = packetUtils.toLocoPacket(1000, "GETCONF", {'os': "win32", "model": "", "MCCMNC": ""})
            ssock.write(packet)

            data = ssock.recv(4096)

            result = packetUtils.readLocoPacket(data)
            return result["Body"]
