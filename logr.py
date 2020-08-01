import os
import time
import socket
import json
import aes

pub = 'MCAwDQYJKoZIhvcNAQEBBQADDwAwDAIFAMg7IrMCAwEAAQ=='
priv = 'MC0CAQACBQDIOyKzAgMBAAECBQCHaZwRAgMA0nkCAwDziwIDAL+xAgJMKwICGq0='
logname = 'hello.log'
commit = os.popen('git rev-parse HEAD').read().strip()
tag = os.popen('git tag -l --points-at HEAD').read().strip()

serverAddressPort = ("127.0.0.1", 7776)
bufferSize = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
cipher = aes.AESCipher(priv)


def log(level, msg):
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
    cipher_log = cipher.encrypt(msg_json)
    print(log_obj)
    print("cipher_log:", json.dumps(cipher_log))
    decrypted = cipher.decrypt(cipher_log)
    print("decrypted:", json.dumps(decrypted))
    data = {
        'public_key': pub,
        'cipher_log': cipher_log
    }
    data_json = json.dumps(data)
    UDPClientSocket.sendto(data_json.encode(), serverAddressPort)
    print("data:", data_json)
