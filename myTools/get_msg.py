from lxml import etree
import requests
import re
import random

def get_ua():
	user_agents = [
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
		'Opera/8.0 (Windows NT 5.1; U; en)',
		'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
		'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
		'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
		'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 ',
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
		'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
		'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
		'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
		'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
		'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0) ',
	]
	user_agent = random.choice(user_agents)
	return {'user-agent': user_agent}

class Yunduanxin(object):
    '''
    初始化需传入参数my_re,即为要提取的验证码的正则表达式
    只提供一个可调用的类方法get_my_msg(num)和一个可调用的类变量useful_list
    get_my_msg(num)返回num收到的符合指定正则的验证码列表（列表成员为字符串）
    useful_list为可用手机号列表（列表成员为字符串）
    具体用法直接拉到代码最底部
    '''
    def __init__(self, my_re):
        self._useful_num = {}
        self._my_re = my_re
        self.useful_list = list(self._get_useful_num())

    def _get_useful_num(self):
        for i in range(1, 11):
            start_url = 'https://www.pdflibr.com/?page=%d' % (i)
            response = requests.get(start_url, headers=get_ua()).text
            html = etree.HTML(response)
            numlist = html.xpath('//h3/text()')
            timelist = html.xpath('//time/text()')
            urllist = html.xpath('//div[@class="sms-number-read col-xs-12 col-sm-12 col-md-4 col-lg-4 margin-3"]/a/@href')
            for num, time, url in zip(numlist, timelist, urllist):
                if ('分钟' in time or '秒' in time) and '+44' not in num:
                    num = num.replace('+86', '')
                    self._useful_num[num] = 'https://www.pdflibr.com' + url
                    yield num

    def get_my_msg(self, num, re_code=False):
        url = self._useful_num[num]
        response = requests.get(url, headers=get_ua()).text
        msg_code = re.findall(re_code or self._my_re, response)
        if len(msg_code) != 0:
            print(num, '收到的的验证码为', msg_code)
            return msg_code
        else:
            print(num, '暂未收到相应短信')
            return False


if __name__ == '__main__':
    test = Yunduanxin(r'【学信网】学历查询短信验证码：(.*?)，有效期15分')
    print(test.useful_list)
    print(test.get_my_msg('19965412404'))