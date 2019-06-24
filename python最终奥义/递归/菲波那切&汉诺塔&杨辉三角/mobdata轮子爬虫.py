import requests
import json
import sys
for i in range(11):
    def spider(url,number,percentage):
        html=requests.get(url)
        hj=html.json()
        const=[]
        for a in range(number):
            age=hj['data']['data'][a]['data'][i][percentage]
            const.append(age)
        return const
    html2=requests.get('https://compass.umeng.com/api/phone/dt?reportId=10010101&platform=all')
    h2=html2.json()
    ds=h2['data']['data'][0]['data'][i]['ds']
    phone=spider('https://compass.umeng.com/api/phone/dt?reportId=10010101&platform=all',2,'percentage')
    sex=spider('https://compass.umeng.com/api/phone/dt?reportId=10010101&sex=all',2,'percentage')
    age=spider('https://compass.umeng.com/api/phone/dt?reportId=10010101&age=all',7,'percentage')
    city=spider('https://compass.umeng.com/api/phone/dt?reportId=10010101&city=all',6,'percentage')
    area=spider('https://compass.umeng.com/api/phone/dt?reportId=10010101&area=all',7,'percentage')
    total=spider('https://compass.umeng.com/api/phone/dt?reportId=10010101',1,'value')
    def pt(classes):
        cla=sys._getframe().f_back.f_locals[classes]
        st=sys._getframe().f_back.f_locals[classes.title()]
        num=len(st)-1
        for b in range(num):
            print(st[0]+'\t'+st[b+1]+'\t'+str(cla[b])+'%\t'+str(ds))
    Phone=['平台','ios','android']
    Sex=['性别','男','女']
    Age=['年龄','<20岁','20-24岁','25-29岁','30-34岁','35-39岁','40-49岁','50岁+']
    City=['城市','一线','二线','三线','四线','五线','六线']
    Area=['区域','华东','华北','华中','华南','西南','西北','东北']
    print('总体'+'\t'+' '+'\t'+str(total[0])+'\t'+str(ds))
    pt('phone')
    pt('sex')
    pt('age')
    pt('city')
    pt('area')
