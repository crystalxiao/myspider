import socket
import re
import logging
import requests
from adsl_py import settings

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=eval('logging.' + settings.LOG_LEVEL),
                    filename=settings.LOG_FILE_NAME)

class ADSL_Server(object):
    def __init__(self, host='localhost', port=9419, timeout=30):
        """
        自动向客户机发送ip地址
        ip需用以下几种方式之一获得:
        1.重写getIP方法
        2.settings中设置ip138的url或token
        """
        self.host = host
        self.port = port
        self.ip = self.getIP()

    def start(self, backlog=5, timeout=3000):
        """
        backlog: 同时挂起的最大连接，默认为5
        timeout: 超时退出，默认为3000(秒)
        """
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(backlog)
        logging.debug('服务器已监理，等待连接...')
        try:
            self.server.settimeout(timeout)
            while True:
                connect, address = self.server.accept()
                while True:
                    data = connect.recv(1024)
                    if data.decode() == 'GET_IP':
                        connect.send(self.getIP().encode('utf-8'))
                        logging.debug('{}已获取ip {}'.format(address, self.ip  ))
                    elif data.decode() == 'EXIT':
                        connect.close()
                        break
        except:
            logging.debug('%d秒内无连接，关闭服务器' % (timeout))
            
    def getIP(self):
        if settings.IP138_TOKEN != None:
            response = requests.get('http://api.ip138.com/query/?token=%s' % (settings.IP138_TOKEN))
            if response.status_code == 200:
                self.ip = re.findall(r'"ip":"(.*?)"', response.text)[0]
            elif settings.IP138_URL == None:
                raise KeyError('token值有误或可用次数不足')
        elif settings.IP138_URL != None:
            response = requests.get(settings.IP138_URL)
            if response.status_code != 200:
                raise KeyError('url有误，请检查url是否过期')
            else:
                self.ip = re.findall(r'IP地址是：\[(.*?)\]', response.text)[0]
        else:
            raise KeyError('请在settings中设置token或url')
        return self.ip