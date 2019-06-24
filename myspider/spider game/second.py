import requests

url = 'http://www.heibanke.com/lesson/crawler_ex01/'
for i in range(0, 31):
    formdata = {'csrfmiddlewaretoken': 'zo1YCSfM6pCZ1Fs6QNuMfB2VkdsNjUsy', 'username': '123', 'password': i}
    reponse = requests.post(url, formdata)
    print(reponse.text)
    if '您输入的密码错误' not in reponse.text:
        print(i)
        break
