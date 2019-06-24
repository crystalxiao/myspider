# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from mafengwo import settings

class MafengwoPipeline(object):
    def process_item(self, item, spider):
        item['name'] = spider.name
        client = pymongo.MongoClient(host=settings.MONGO_HOST, port= settings.MONGO_PORT)
        db = client.mafengwo
        dbdata = db.data
        dbdata.insert(item)
        client.close()
        return item
