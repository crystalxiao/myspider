#encoding=utf-8
import scrapy
from news_spider.items import NewsSpiderItem
import json
import time 
import re

class TencentSpider(scrapy.Spider):

	start_urls = ['http://news.qq.com']
	name='tencent'
	allowed_domains=['news.qq.com']

	base_url = 'http://news.qq.com/b/history/index'
#	year = ['2019','2018']
#	month = ['0' + str(i) for i in range(1, 10)] + ['10', '11', '12']
#	day = ['0' + str(i) for i in range(1, 10)] + [str(i) for i in range(10, 32)]
	tp = ['am','pm']

	day = ['0' + str(i) for i in range(1, 10)] + [str(i) for i in range(10, 32)]
	year = ['2019']
	month = ['0' + str(i) for i in range(1, 10)] + ['10', '11', '12']

	def parse(self,response):
		for y in self.year:
			for m in self.month:
				for d in self.day:
					for t in self.tp:
						url = self.base_url+y+m+d+t+'.shtml?'
						yield scrapy.Request(url,self.parseList)

	
	def parseList(self,response):
        if response.status != 200:
    	    return None
		urls = response.xpath("//a/@href").extract()
		for url in urls:
			if 'http' in url:
				yield scrapy.Request(url,self.parseNews)

	def parseNews(self,response):
		data = response.xpath("//div[@id='C-Main-Article-QQ']")
		item = NewsSpiderItem()
		timee = data.xpath("//span[@class='article-time']/text()").extract()
		title = data.xpath("//div[@class='hd']//h1/text()").extract()
		content = data.xpath("//p/text()").extract()

		time_pattern = re.compile("[0-9]{4}-[0-9]{2}-[0-9]{2}\s[0-9]{2}:[0-9]{2}")
		if(len(timee)!=0 and len(title)!=0 and len(content)!=0):
			tm = time_pattern.findall(timee[0])[0]
			item['time'] = int(time.mktime(time.strptime(tm,'%Y-%m-%d %H:%M')))
			item['title'] = title[0]
			item['url'] = response.url
			item['the_from'] = 'Tencent'
			cc=''
			if(len(content)!=0):
				for c in content:
					cc = cc+c+'\n'
			item['content'] = cc
			yield item