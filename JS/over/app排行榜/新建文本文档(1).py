import requests
import json
from lxml import etree
import os
from prettytable import PrettyTable
doc = open("out.xls",'w')
x = PrettyTable(["app名字","app分类"])
def getonepage(n):
    url = f'http://index.iresearch.com.cn/app/GetDataList/?classId=0&classLevel=0&timeId=70&orderBy=2&pageIndex='+str(n)
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    r = requests.get(url, headers=header)
    a = r.json()
    return a 
name_list=[]
for i in range(1,10):
    message=getonepage(i)
    data_list=message['List']
    for data_dic in data_list:
        #name_list.append(data_dic['AppName'])
        #name_list=name_list+[data_dic['AppName']]
        #print(name_list,)
        #doc.close()
        x.add_row([data_dic['AppName'],data_dic['KclassName']])
print(x,file=doc)
doc.close()
