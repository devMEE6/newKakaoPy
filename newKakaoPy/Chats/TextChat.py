from .BaseChat import BaseChat

class TextChat(BaseChat):
    def __init__(self, message):
        self.message = message
       
    def getType(self):
        return 1
        
    def getAttachment(self):
        return "{}"
        
    def getMessage(self):
        return self.message
        
        
