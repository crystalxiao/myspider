# coding=utf-8


import time
import json

with open("config", 'r', encoding='utf8') as f:
    config = json.loads(f.read())


def send_msg(bor):
    try:
        time.sleep(1)
        bor.find_elements_by_class_name("house-chat-im")[0].click()
        time.sleep(0.8)
        bor.switch_to_frame("webimIframe")
        time.sleep(0.8)
        bor.execute_script("$('.im-input-richtext').text('{0}')".format(config.get('msg')))
        time.sleep(0.8)
        bor.find_elements_by_class_name("im-send")[0].click()
        print("发送成功,执行下一条...")
    except Exception as f:
        pass
    time.sleep(1)
    bor.close()
