from lxml import etree
import time
import subprocess
import platform
import logging
import re
import sys
import requests

#adsl拨号的用户名，账号及密码
ADSL_NAME = '宽带连接'
ADSL_USER = '9854645112'
ADSL_PASSWORD = '369258'

#ip138的查询ip的url及接口，优先调用接口
IP138_URL = '200019.ip138.com'
IP138_TOKEN = None

#日志的输出控制
LOG_FILE_NAME = 'log.log'
LOG_LEVEL = 'DEBUG'

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=eval('logging.' + LOG_LEVEL),
                    filename=LOG_FILE_NAME)

class ADSL_Tool(object):
    def __init__(self):
        self.sys = platform.system()
        self.name = ADSL_NAME
        self.url = IP138_URL
        self.token = IP138_TOKEN
        self.user = ADSL_USER
        self.password = ADSL_PASSWORD
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

mynet = ADSL_Tool()
mynet.connect()
#url = "http://glidedsky.com/level/web/crawler-basic-2?page=1"

#cookie = "id=220654ca3cc00000||t=1563078038|et=730|cs=002213fd481332ded4e23be1cd"

L=[]
headers = {
            
        "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
        #"Accept-Encoding": "gzip, deflate",        
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Cookie": "_ga=GA1.2.1761931703.1564386624; _gid=GA1.2.1386176686.1564386624; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1564386624; XSRF-TOKEN=eyJpdiI6IjlXVFF4UVBQazkweWhvSjZNOXh4ZkE9PSIsInZhbHVlIjoiaEVjRDgyMmxDUFFJYWtmMm9Dc0dMRFFQcFE5aUEzTGVVOXAyXC9rXC9TQmcyUHpqK0JkRm1ZU1FSbllNeWd4N05oIiwibWFjIjoiZWZlNzY0YTI3OWMyODcxOWNmNjYxZWNlZmQ2ZjRlZmQ5NzkxODQ1NzdmMDgwN2VlNTE1OTExYzVjYzY1M2Y1NCJ9; glidedsky_session=eyJpdiI6ImFHbVJIVHNPXC84RlNZVzl0cjJlNnZ3PT0iLCJ2YWx1ZSI6IlpRUGRmaWI5OWN2bnp4MmsyV252eXpNUmg4a2R6XC9iVFF6Y21BdFE5bHNuU2RXWngrbGVtVG50T0VtbVhkOTRjIiwibWFjIjoiNTQyM2ZjMGQyYTg1NTYyYThiY2RkMjJmODNlMWJhMmM0MzExYzJmOTA1NmZhODczYTNiYWQ3OGI1NjVmYjUyYyJ9; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1564394008; _gat_gtag_UA_75859356_3=1",
        "Host": "glidedsky.com",
        "Pragma": "no-cache",
        "Referer": "http://glidedsky.com/level/web/crawler-basic-2?page=1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}
#content = requests.post(url, headers=headers, data=data, params=params)

def getPage(url):
    # res = requests.post(url,headers=self.headers,data=form)
    # print(res.url)
    # html = res.text
    while True:
        try:
            response = requests.get(url, headers=headers)
            if key.status_code != 200:
                raise Exception
            response = response.content
            break
        except:
            continue
    
    html=response.text
    print(html)
    parsePage(html)


def parsePage(html):
    parseHtml = etree.HTML(html)
    number = parseHtml.xpath('//div[@class="col-md-1"]/text()')
  
    
    a = [' '.join([i.strip() for i in price.strip().split("\n")]) for price in number]
    #c = [' '.join([i.strip() for i in price.strip().split("''")]) for price in number]
    c = list(map(lambda x:int(x),a))
    b = sum(c)
    L.append(b)
    s = sum(L)
    
    print(s)


def workOn():
        begin =int(input("起始页："))

        end = int(input("终止页："))
        
        for i in range(begin,end+1):
            #url = "http://glidedsky.com/level/web/crawler-basic-2?page=" + str(i)
            url = "http://glidedsky.com/level/web/crawler-ip-block-1?page=" + str(i)
            mynet.reconnect()
            #time.sleep(2)
            
            logging.debug('正在爬取------page %s-------' % i) #打印当面爬取的页码

            getPage(url)
        
        logging.debug("爬取结束")
  


workOn()