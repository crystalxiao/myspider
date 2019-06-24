import requests
import re

url = 'http://www.heibanke.com/lesson/crawler_ex00/'
new_url = url
number = 99999

while number:
    response = requests.get(new_url)
    print(response.text)
    number = re.findall(r'<h3>.*?(\d+).*?</h3>',response.text)[0]
    print(number)
    new_url = url + number

print('下一关')