import hashlib
   
def getXVC(email, device_uuid, authAgent, isFull=False):
    Hash = hashlib.sha512("HEATH|{}|DEMIAN|{}|{}".format(
        authAgent, email, device_uuid).encode("utf-8")).hexdigest()
    if isFull:
        return Hash
    return Hash[0:16]
