"""
解析js，破解加密
"""

import execjs
import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'https://www.qimai.cn',
    'Referer': 'https://www.qimai.cn/rank/index/brand/grossing/device/iphone/country/cn/genre/5000/date/2019-06-29',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
}

def get_synct():
    resp = requests.get('https://www.qimai.cn/rank', headers=headers)
    cookies = resp.cookies.get_dict()
    synct = cookies.get('synct')
    return cookies, synct

def get_analysis(params, synct):
    """
    获取加密参数analysis
    """
    with open('./qimai/analysis.js', 'rb') as f:
        js = f.read().decode()
    ctx = execjs.compile(js)
    analysis = ctx.call('getAnalysis', params, synct)
    return analysis

def process_params(params):
    """
    对加密参数进行排序, 构造加密字符串
    """
    params_ = []
    for value in params.values():
        params_.append(value)
    p_str = ''
    # 对参数列表进行排序
    params_.sort()
    for p in params_:
        p_str += p
    return p_str
