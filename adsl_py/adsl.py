import subprocess
import platform
import logging
import re
import sys
import requests
from adsl_py import settings

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=eval('logging.' + settings.LOG_LEVEL),
                    filename=settings.LOG_FILE_NAME)

class ADSL_Tool(object):
    def __init__(self, netName='adslproxy', user=None, password=None, url=None, token=None):
        """
        user: windows使用者的adsl用户账号
        password: windows使用者的adsl密码
        url: ip138的ip查询临时url
        token: ip138提供的ip查询接口
        当同时使用了url与token参数，默认会调用token返回ip地址
        """
        self.sys = platform.system()
        self.name = netName or settings.ADSL_NAME
        self.url = url or settings.IP138_URL
        self.token = token or settings.IP138_TOKEN
        self.user = user or settings.ADSL_USER
        self.password = password or settings.ADSL_PASSWORD
        self.ip = self.refreshIP()
        self.status = False
        if self.sys == 'Windows':
            self.connect_commands = 'rasdial %s %s %s' % (self.name, self.user, self.password)
            self.disconnect_commands = 'rasdial ' + self.name + ' /disconnect'
        elif self.sys == 'Linux':
            self.connect_commands = 'ifup ' + self.name
            self.disconnect_commands = 'ifdown ' + self.name
        else:
            raise Exception('ADSL_Tool 目前仅用于windows或linux系统')
    
    def cmd(self, commands):
        """
        commands : 命令行指令, type：str
        return : 终端输出内容, type: str
        """
        try:
            status, output = subprocess.getstatusoutput(commands)
            if status == 0:
                return output
            else:
                raise Exception
        except:
            logging.error('Failed to run the commands "%s"' % (commands))

    def connect(self):
        """
        return : adsl拨号后的IP值, type: str
        """
        if not self.status:
            logging.debug(self.cmd(self.connect_commands))
            self.ip = self.refreshIP()
            self.status = True
            return self.ip
        else:
            raise Exception('当前处于已连接状态, 请断开后重连')

    def disconnect(self):
        """
        取消连接，return值为0表示取消成功
        """
        if self.status:
            logging.debug(self.cmd(self.disconnect_commands))
            self.ip = self.refreshIP()
            self.status = False
            return 0
        else:
            raise Exception('当前已处于未连接状态')

    def reconnect(self):
        """
        重新拨号
        return : 重播后的ip值, type: str
        """
        if self.status:
            logging.debug(self.cmd(self.disconnect_commands))
        else:
            raise Exception('当前处于未连接状态，不可重新拨号')
        return self.connect()

    def refreshIP(self):
        """
        return : 当前网络的IP值, type: str
        """
        if self.token != None:
            response = requests.get('http://api.ip138.com/query/?token=%s' % (self.token))
            if response.status_code == 200:
                self.ip = re.findall(r'"ip":"(.*?)"', response.text)[0]
            elif self.url == None:
                raise KeyError('token值有误或可用次数不足')
        elif self.url != None:
            response = requests.get(self.url)
            if response.status_code != 200:
                raise KeyError('url有误，请检查url是否过期')
            else:
                self.ip = re.findall(r'IP地址是：\[(.*?)\]', response.text)[0]
        else:
            raise KeyError('请输入token或url')
        return self.ip