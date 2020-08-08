import time
import json


class Logger:

    def __init__(self, config, logname):
        self.config = config
        self.logname = logname

    def log(self, level, msg):
        ts = str(time.time_ns())
        log_obj = {
            'timestamp': ts,
            'hostname': self.config.hostname,
            'logname': self.logname,
            'level': level,
            'pid': self.config.pid,
            'version': self.config.getversion(),
            'message': msg
        }
        msg_json = json.dumps(log_obj)
        cipher_log = self.config.cipher.encrypt(msg_json)
        data = {
            'public_key': self.config.public_key,
            'cipher_log': cipher_log
        }
        data_json = json.dumps(data)
        self.config.client.sendto(data_json.encode(), self.config.udp)
        print(data_json)
