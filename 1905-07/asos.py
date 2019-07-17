import requests
from lxml import etree
from bs4 import BeautifulSoup
import os
import re

#更新价格，改为True只更新价格
price_update = False

def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path) 
        print(path+' 创建成功')
        return True
    else:
        print(path+' 目录已存在')
        return False

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36','accept-language': 'zh-CN,zh;q=0.9'}
detail_dic = {}

def myparse(det_url, price):
    response = requests.get(url=det_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    res = etree.HTML(soup.prettify())
    img = res.xpath('//div[@class="thumbnails"]/ul/li/a/img/@src')
    title = res.xpath('//span[@itemprop="name"]/text()')[1]
    productID = res.xpath('//span[@itemprop="productID"]/text()')[0]
    prices = float(price.strip()[1:]) * 9.00892
    #prices = float(res.xpath('//span[@itemprop="price"]/text()')[0]) * 4.862
    m3u8 = 'https://video.asos-media.com/products/%s/%s-catwalk-AVS.m3u8' % (title.strip().lower().replace(' ', '-').replace('&', ''), productID.strip())
    # print(m3u8)
    video_url = 'https://video.asos-media.com/products/' + re.findall(r'ASOS.*?mp4', requests.get(url=m3u8, headers=headers).text)[0]
    mkdir('data/%s' % title.strip())
    for i in range(1, 5):
        small_img_path = 'data/%s/small_%d.jpg' % (title.strip(), i)
        big_img_path = 'data/%s/big_%d.jpg' % (title.strip(), i)
        if not os.path.exists(small_img_path):
            with open(small_img_path, 'wb') as f:
                f.write(requests.get(url=img[i-1], headers=headers).content)
        if not os.path.exists(big_img_path):
            with open(big_img_path, 'wb') as f:
                big_url = re.findall(r'http.*?\?', img[i-1])[0] + '?$XXL$&wid=513&fit=constrain'
                # print(big_url)
                f.write(requests.get(url=big_url, headers=headers).content)
    print('图片写入成功')
    price_path = 'data/%s/name_and_price.txt' % (title.strip())
    if price_update or (not os.path.exists(price_path)):
        with open(price_path, 'w', encoding='utf8') as f:
            f.write('名字:%s \n价格:%.2f' % (title.strip(), prices))
    print('价格写入成功')
    video_path = 'data/%s/video.mp4' % (title.strip())
    if not os.path.exists(video_path):
        with open(video_path, 'wb') as f:
            f.write(requests.get(url=video_url, headers=headers).content)
    print('视频写入成功')

mkdir('data')

for i in range(1, 20):
    print('正在读取第%d页数据' % i)
    url = 'https://www.asos.com/men/jackets-coats/cat/?cid=3606&nlid=mw|clothing|shop%20by%20product&page=' + str(i)
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        res = etree.HTML(soup.prettify())
        detail_url = res.xpath('//article/a/@href')
        price = res.xpath('//span[@data-auto-id="productTilePrice"]/text()')
        if detail_url[0] in detail_dic:
            break
        for k, v in zip(detail_url, price):
            detail_dic[k] = v
print('正在写入数据')
c = 1
for det_url, price in detail_dic.items():
    print('进度:%.2f%%' % (c/len(detail_dic) * 100))
    c += 1
    # print(det_url)
    try:
        myparse(det_url, price)
    except:
        myparse(det_url, price)