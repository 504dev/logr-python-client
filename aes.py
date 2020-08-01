import json
import base64
import hashlib
from Cryptodome import Random
from Cryptodome.Cipher import AES


class AESCipher(object):

    def __init__(self, key):
        self.bs = AES.block_size
        key_bytes = base64.b64decode(key)
        self.key = hashlib.sha256(key_bytes).digest()
        print(key, self.key.hex(), AES.block_size)

    def encrypt(self, raw):
        # raw = 'world'
        iv = Random.new().read(AES.block_size)
        # iv = b'0123456789ABCDEF'
        cipher = AES.new(self.key, AES.MODE_CFB, iv)
        print(000, raw.encode())
        encrypted = cipher.encrypt(raw.encode())
        print(111, json.dumps(base64.b64encode(iv).decode()))
        print(222, json.dumps(base64.b64encode(encrypted).decode()))
        return base64.b64encode(iv + encrypted).decode()

    def decrypt(self, enc):
        enc = base64.b64decode(enc.encode())
        iv = enc[:AES.block_size]
        body = enc[AES.block_size:]
        print(333, json.dumps(base64.b64encode(iv).decode()))
        print(444, json.dumps(base64.b64encode(body).decode()))
        cipher = AES.new(self.key, AES.MODE_CFB, iv)
        return cipher.decrypt(body).decode()

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])]
