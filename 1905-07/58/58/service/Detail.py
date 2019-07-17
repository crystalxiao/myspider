# coding=utf-8
import json
import time

from bs4 import BeautifulSoup

with open("config", 'r', encoding='utf8') as f:
    config = json.loads(f.read())


def select(bor):
    bor.find_elements_by_class_name("secitem")[0].find_element_by_tag_name("dd").find_elements_by_tag_name("a")[
        config.get('area')].click()
    bor.find_elements_by_class_name("secitem")[1].find_element_by_tag_name("dd").find_elements_by_tag_name("a")[
        config.get('zujin')].click()
    bor.find_elements_by_class_name("secitem")[2].find_element_by_tag_name("dd").find_elements_by_tag_name("a")[
        config.get('tingshi')].click()
    bor.find_elements_by_class_name("secitem")[3].find_element_by_tag_name("dd").find_elements_by_tag_name("a")[
        config.get('fangshi')].click()


def get_list(bor):
    html = bor.page_source
    doc = BeautifulSoup(html, 'lxml')
    list_house = doc.select(".house-list")[0]
    url_list = []
    for oneli in list_house.select('.img-list'):
        url = oneli.select("a")[0].attrs['href']
        if url.find("legocli") == -1:
            url_list.append(url)
    return url_list


def next_page(bor):
    try:
        bor.find_elements_by_class_name("next")[0].click()
        time.sleep(1)
        return True
    except Exception as f:
        print(f)
        return False
