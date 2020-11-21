from newKakaoPy.kakaoPy import kakaoPy
from newKakaoPy.Chats.TextChat import TextChat

app = kakaoPy("uid", "upw", "dname", "duuid")

@app.packetReceive("ALL")
async def packetReceive(packet):
    print(packet)
    
@app.messageReceive()
async def messageReceiver(message):
    print(message.message)
    
    if p.message == ".TEST":
        await message.sendChat(TextChat("HELLO"))
         
app.run()
