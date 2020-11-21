def getMessageData(body):
    if "attachment" in body["chatLog"]:
        if body["chatLog"]["attachment"] != "":
            attachment = {}
        else:
            attachment = body["chatLog"]["attachment"]
    else:
        attachment = {}
        
    return {
        "chatId":body["chatLog"]["chatId"],
        "msgId":body["chatLog"]["msgId"],
        "logId":body["chatLog"]["logId"],
        "prevId":body["chatLog"]["prevId"],
        "sendAt":body["chatLog"]["sendAt"],
        "type":body["chatLog"]["type"],
        "senderId":body["chatLog"]["authorId"],
        "senderName":body["authorNickname"],
        "message":body["chatLog"]["message"],
        "attachment":attachment,
    }
        
    
