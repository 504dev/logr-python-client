import os
import time
import socket
import json
import aes
import hashlib
import base64

commit = os.popen('git rev-parse HEAD').read().strip()
tag = os.popen('git tag -l --points-at HEAD').read().strip()

udp = ("127.0.0.1", 7776)
pub = 'MCAwDQYJKoZIhvcNAQEBBQADDwAwDAIFAMg7IrMCAwEAAQ=='
priv = 'MC0CAQACBQDIOyKzAgMBAAECBQCHaZwRAgMA0nkCAwDziwIDAL+xAgJMKwICGq0='
logname = 'hello.log'


class Logr(object):

    def __init__(self, private_key):
        key_bytes = base64.b64decode(private_key)
        self.private_hash = hashlib.sha256(key_bytes).digest()
        self.cipher = aes.AESCipher(self.private_hash)
        self.client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    def log(self, level, msg):
        ts = str(time.time_ns())
        log_obj = {
            'timestamp': ts,
            'hostname': socket.gethostname(),
            'logname': logname,
            'level': level,
            'pid': os.getpid(),
            'version': tag or commit,
            'message': msg
        }
        msg_json = json.dumps(log_obj)
        cipher_log = self.cipher.encrypt(msg_json)
        data = {
            'public_key': pub,
            'cipher_log': cipher_log
        }
        data_json = json.dumps(data)
        self.client.sendto(data_json.encode(), udp)
        print("data:", data_json)
