from newKakaoPy.kakaoPy import kakaoPy
from newKakaoPy.Chats.TextChat import TextChat

app = kakaoPy("uid", "upw", "dname", "duuid")

@app.packetReceive("ALL")
async def packetReceive(packet):
    print(packet)
    
@app.messageReceive()
async def messageReceiver(chat):
    print(chat.message)
    
    if chat.message == ".TEST":
        await chat.sendChat(TextChat("HELLO"))
         
app.run()
