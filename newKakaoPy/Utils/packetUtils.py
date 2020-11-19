import io
import bson
import struct

def toLocoPacket(packet_id, packet_name, body):
    bson_body = bson.dumps(body)
    
    f = io.BytesIO()
    f.write(struct.pack("<I", packet_id))
    f.write(struct.pack("<H", 0))

    if (11-len(packet_name)) < 0:
        raise Exception("invalid packet name length")

    f.write(packet_name.encode("utf-8"))

    f.write(b"\x00"*(11-len(packet_name)))
    f.write(struct.pack("<b", 0))
    f.write(struct.pack("<i", len(bson_body)))

    f.write(bson_body)
    return f.getvalue()
    
def readLocoPacket(packet):
    return {
        "PacketID":struct.unpack("<I", packet[:4])[0],
        "StatusCode":struct.unpack("<H", packet[4:6])[0],
        "PacketName":packet[6:17].decode("utf-8").replace("\0", ""),
        "BodyType":struct.unpack("<b", packet[17:18])[0],
        "BodySize":struct.unpack("<i", packet[18:22])[0],
        "Body":bson.loads(packet[22:]),
    }
    
    
