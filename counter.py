import threading
import socket
import json
from logr import Logr


class Counter:

    def __init__(self, config: Logr, logname):
        self.config = config
        self.logname = logname
        self.conn = None
        self.tmp = {}
        self.timer = None

    def connect(self):
        if self.conn is None:
            self.conn = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    def run(self, interval):
        if self.timer is None:
            self.timer = threading.Timer(interval, self.flush)
            self.timer.start()

    def flush(self):
        for key in self.tmp:
            value = self.tmt.get(key)
            self.send(value)

    def stop(self):
        self.flush()

    def send(self, data):
        cipher_count = self.config.cipher.encrypt(json.dumps(data))
        pack = {
            'public_key': self.config.public_key,
            'cipher_count': cipher_count
        }
        self.conn.sendto(json.dumps(pack).encode(), self.config.udp)

    def blank(self):
        return {
            'hostname': self.config.hostname,
            'logname': self.logname,
            'version': self.config.getversion(),
        }

    def touch(self, keyname):
        self.connect()
        self.run(20)
        if self.tmp.get(keyname) is None:
            self.tmp[keyname] = {}
        return self.tmp[keyname]
