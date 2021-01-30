from newKakaoPy.Chats.TextChat import TextChat
from newKakaoPy.kakaoPy import kakaoPy

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
