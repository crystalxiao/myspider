# coding=utf-8


from selenium import webdriver
from service.Detail import *
from service.SendMsg import *
import json
from setting import citylist

with open('config', 'r', encoding='utf8') as f:
    config = json.loads(f.read())

def run():
    driverOptions = webdriver.ChromeOptions()
    driverOptions.add_argument(r"user-data-dir=.\userData")
    bor = webdriver.Chrome()
    url = "https://%s.58.com/chuzu/0/" % (citylist[config['city']])
    # print(url)
    bor.get(url)
    input("登陆完账号回车:")
    return bor


if __name__ == '__main__':
    bor = run()
    select(bor=bor)  # 筛选
    url_list = get_list(bor=bor)
    # print(url_list)
    page = 1
    main_handle = bor.current_window_handle
    while page == 1 or next_page(bor):
        for one_url in url_list:
            bor.switch_to.window(main_handle)
            bor.execute_script('window.open("{0}");'.format(one_url))
            time.sleep(1)
            handles = bor.window_handles
            detail_handle = None
            for handle in handles:
                if handle != bor.current_window_handle:
                    detail_handle = handle
            bor.switch_to.window(detail_handle)
            send_msg(bor=bor)
        page = page + 1
        bor.switch_to.window(main_handle)
        print("开始下一页:{0}".format(page))
