from .Utils import packetUtils
from .Config import BookingURL, BookingPort
import socket
import ssl

def getBookingData():
    context = ssl.create_default_context()

    with socket.create_connection((BookingURL, BookingPort)) as Socket1:
        with context.wrap_socket(Socket1, server_hostname=BookingURL) as Socket2:
            packet = packetUtils.toLocoPacket(1000, "GETCONF", {'os': "win32", "model": "", "MCCMNC": ""})
            Socket2.write(packet)

            data = Socket2.recv(4096)

            result = packetUtils.readLocoPacket(data)
            return result["Body"]
