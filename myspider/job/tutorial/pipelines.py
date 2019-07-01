# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import datetime
from scrapy.conf import settings

# 学历列表
educations = ("不限","大专","本科","硕士","博士")
#部分不一致学历需要修改
def clean_education(edu,body):
    if edu not in educations:
        for i in educations:
            if i in body:
                edu = i
            else:
                edu = '不限'
    return edu

#薪水
def clear_salary(salary):
    res = salary.split("-")
    temp = []
    for x in res:
        temp.append(int(x.upper().replace("K"," "))*1000)
    result = {
        "min":temp[0],
        "max":temp[1],
        "avg":int((temp[0]+temp[1])/2)
    }
    return result

#时间
def clear_time(time):
    now_year = datetime.datetime.now().year
    if '发布于' in  time:
        time = time.replace("发布于", str(now_year)+"-")
        time = time.replace("月", "-")
        time = time.replace("日", "")
        if time.find("昨天") > 0:
            time = str(datetime.date.today() - datetime.timedelta(days=1))
        elif time.find(":") > 0:
            time = str(datetime.date.today())
    return time

#工作地点
def clear_position(name):
    data =  name.split(" ")
    name = data[0]
    work_year = data[-2]
    educational = data[-1]
    return name,work_year,educational

#判断python是否在职位名称中，不在就过滤掉
def clean_name(name):
    if 'python' not in name.upper():
        return False
    return True

#向mongodb插入数据
class TutorialPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host="127.0.0.1", port=27017)

    def process_item(self, item, spider):
        db = self.client['job']
        collection =  db['position2']
        collection.insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()

#处理直聘网数据
class ZhipinPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host='127.0.0.1', port=27017)

    def process_item(self, item, spider):
        db = self.client['job']
        collection =  db['position']
        item['salary'] = clear_salary(item['salary'])
        item['create_time'] = clear_time(item['create_time'])
        item['educational'] = clean_education(item['educational'],item['body'])
        is_php = clean_name(item['position_name'])
        if is_php is True:
            collection.insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()


#处理51job数据
class FiveJobPipeline(object):
    def clear_salary(self,salary):
        lists = salary.split('/')[0].split('-')
        themin, themax = lists
        if '千' in themax:
            unit = 1000
            themax = themax.replace('千','')
        else:
            unit = 10000
            themax = themax.replace('万','')
        print(themax)
        result = {}
        result['min'] = float(themin)*unit
        result['max'] = float(themax)*unit
        result['avg'] = (result['max']+result['min'])/2
        return result

    def clear_address(self,address):
        if '上班地址' in address:
            address = address.replace('上班地址 :','')
        return address

    def clear_workyear(self,work_year):
        if '经验' in work_year:
           work_year =  work_year.replace('工作经验','') or work_year.replace('经验','')
        return work_year
        
    def process_item(self, item, spider):
        client = pymongo.MongoClient(host="127.0.0.1", port=27017)
        db = client['job']
        collection =  db['51job']
        item['salary'] = self.clear_salary(salary=item['salary'])
        item['address'] = self.clear_address(address=item['address'])
        item['work_year'] = self.clear_workyear(work_year=item['work_year'])
        collection.insert(dict(item))
        client.close()
        return item
