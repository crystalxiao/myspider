import socket
import logging
import re
from adsl_py import settings

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=eval('logging.' + settings.LOG_LEVEL))

class ADSL_Client(object):
    def __init__(self, host=SERVER_HOST, port=9419):
        self.host = host
        self.port = port

    def connect(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))

    def getIP(self):
        self.client.send('GET_IP'.encode('utf-8'))
        data = self.client.recv(1024)
        self.ip = data.decode()
        if re.findall(r'(?:\d{1,3}\.){3}\d{1,3}', self.ip)[0] == self.ip:
            logging.debug('获得代理ip: %s' % (self.ip))
            return self.ip
        else:
            logging.error('获得了错误的代理ip: %s' % (self.ip))

    def close(self):
        self.client.send('EXIT'.encode('utf-8'))
        self.client.close()
        