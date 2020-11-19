from newKakaoPy.kakaoPy import kakaoPy
from newKakaoPy.Packets.MsgPacket import MsgPacketRes
from newKakaoPy.Packets.WritePacket import WritePacketReq

app = kakaoPy("uid", "upw", "dname", "duuid")

@app.receive("MSG", MsgPacketRes)
async def msg_receiver(msg):
    print(msg.message)
    if msg.message == "WA?":
        print(await app.sendPacket(WritePacketReq(msg.chatId, {}, 1, 1, "SANZ!!!", False)))
    
app.run()
