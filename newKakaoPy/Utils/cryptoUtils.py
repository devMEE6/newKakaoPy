import os
import struct

from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Hash import SHA1
from Crypto.PublicKey import RSA
from Crypto.Signature import pss

from ..Config import RSASeed


def getRandomAesKey():
    return os.urandom(16)
    
def getLocoRsaPublicKey():
    n = int(RSASeed[0], 16)
    e = int(RSASeed[1], 16)

    rsa_key = RSA.construct((n, e))
    return rsa_key

def rsaEncrypt(data):
    rsa_key = getLocoRsaPublicKey()
    rsa_cipher = PKCS1_OAEP.new(key=rsa_key, hashAlgo=SHA1, mgfunc=lambda x, y: pss.MGF1(x, y, SHA1))

    return rsa_cipher.encrypt(data)

def aesEncrypt(data, key, iv):
    aes_cipher   = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
    return aes_cipher.encrypt(data)

def aesDecrypt(data, key, iv):
    aes_cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
    return aes_cipher.decrypt(data)
    
def encryptPacket(packet_bytes, key):
    iv = os.urandom(16)

    encrypted_packet = aesEncrypt(packet_bytes, key, iv)

    buf = b""
    buf += struct.pack("<I", len(encrypted_packet)+len(iv))
    buf += iv
    buf += encrypted_packet

    return buf
        
def decryptPacket(packet_bytes, key):
    packetLen = struct.unpack(">I", packet_bytes[0:4])[0]
    iv = packet_bytes[4:20]
    data = packet_bytes[20:packetLen-16]

    dec = aesDecrypt(data, key, iv)

    return dec
    
def getHandshakePacket(aes_key):
    encrypted_key = rsaEncrypt(aes_key)
    
    buf = b""
    buf += struct.pack("<I", len(encrypted_key))
    buf += struct.pack("<I", 12)
    buf += struct.pack("<I", 2)
    buf += encrypted_key

    return buf
