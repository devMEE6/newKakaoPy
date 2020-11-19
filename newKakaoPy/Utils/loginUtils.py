import hashlib
   
def getXVC(email, device_uuid, authAgent, isFull=False):
    hash = hashlib.sha512("HEATH|{}|DEMIAN|{}|{}".format(
        authAgent, email, device_uuid).encode("utf-8")).hexdigest()
    if(isFull):
        return hash
    return hash[0:16]
