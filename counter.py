import threading
import socket
import json
from logr import Logr
from count import Count


class Counter:

    def __init__(self, config: Logr, logname: str):
        self.config = config
        self.logname = logname
        self.conn = None
        self.tmp = {}
        self.timer = None

    def connect(self):
        if self.conn is None:
            self.conn = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    def run(self, interval: int):
        if self.timer is None:
            self.timer = threading.Timer(interval, self.flush)
            self.timer.start()

    def flush(self):
        for key in self.tmp:
            value = self.tmp.get(key)
            self.send(value)

    def stop(self):
        self.flush()

    def send(self, data: Count):
        cipher_count = self.config.cipher.encrypt(data.tojson())
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

    def touch(self, keyname: str) -> Count:
        self.connect()
        self.run(20)
        if self.tmp.get(keyname) is None:
            count = Count({'keyname': keyname, **self.blank()})
            self.tmp[keyname] = count
        return self.tmp[keyname]

    def inc(self, key: str, num: float = 1):
        return self.touch(key).inc(num)

    def max(self, key: str, num: float):
        return self.touch(key).max(num)

    def min(self, key: str, num: float):
        return self.touch(key).min(num)

    def avg(self, key: str, num: float):
        return self.touch(key).avg(num)

    def per(self, key: str, taken: float, total: float):
        return self.touch(key).per(taken, total)

    def time(self, key: str, duration: int):
        return self.touch(key).time(duration)
