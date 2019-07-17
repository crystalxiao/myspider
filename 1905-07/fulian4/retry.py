import re
import os
import requests
import logging
from fulian4 import url2video

logging.basicConfig(filename='fail_file.log')

with open('log.log', 'r') as f:
    data = f.read()

url_p = r'http.*?\.ts'
file_p = r'个(.*?ts)'
url_list = re.findall(url_p, data)
file_list = re.findall(file_p, data)

for i in range(len(url_list)):
    url2video(url_list[i], file_list[i])