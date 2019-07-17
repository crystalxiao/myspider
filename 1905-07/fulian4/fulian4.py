import requests
import re
from time import sleep
import os
from multiprocessing import Pool
import logging

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}

logging.basicConfig(filename='log.log')

def url2video(url, file_path):
    with open(file_path, 'wb') as f:
        try:
            response = requests.get(url=url, headers=headers, timeout=5)
            video = response.content
            f.write(video)
            print(url + '写入成功')
        except:
            print(url + '写入失败，下一个')
            logging.warning(url + '写入失败，下一个' + file_path)

if __name__ == '__main__':
    pool = Pool()
    m3u8_url = 'https://vs1.baduziyuan.com/ppvod/801FE2CE7C5BA7ABC30DEAAC2BA53C68.m3u8'
    response = requests.get(url=m3u8_url, headers=headers)
    m3u8 = response.text

    p = r'\b/.*?ts\b'
    urllist = re.findall(p, m3u8)
    l = len(urllist)
        
    for i in range(l):
        ts_path = '%d.ts' % i
        if not os.path.exists(ts_path):
            ts_url = 'https://vs1.baduziyuan.com/20190424' + urllist[i]
            pool.apply_async(url2video, (ts_url, ts_path))
            # sleep(1)
    
    pool.close()
    pool.join()