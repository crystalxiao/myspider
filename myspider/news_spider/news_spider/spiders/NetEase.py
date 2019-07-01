import json
import re
import time

import scrapy

from news_spider.items import NewsSpiderItem


class NetEaseSpider(scrapy.Spider):

	start_urls = ['http://snapshot.news.163.com/wgethtml/http+!!news.163.com!/2019-01/17/12.html']
	name='netease'
	allowed_domains=['news.163.com']

	base_url = 'http://snapshot.news.163.com/wgethtml/http+!!news.163.com!'
#	year = ['2019','2018']
#	month = ['0' + str(i) for i in range(1, 10)] + ['10', '11', '12']
#	day = ['0' + str(i) for i in range(1, 10)] + [str(i) for i in range(10, 32)]
	year = ['2019']
	month = ['01']
	day = [str(i) for i in range (21, 32)]

	def parse(self,response):
		for y in self.year:
			for m in self.month:
				for d in self.day:
					url = self.base_url+'/'+y+'-'+m+'/'+d+'/12.html'
					yield scrapy.Request(url,self.parseList)

	
	def parseList(self,response):
		urls = response.xpath("//a/@href").extract()
		for url in urls:
			yield scrapy.Request(url,self.parseNews)

	def parseNews(self,response):
		data = response.xpath("//div[@class='post_content_main']")
		item = NewsSpiderItem()
		timee = data.xpath("//div[@class='post_time_source']/text()").extract()
		title = data.xpath("//h1/text()").extract()
		content = data.xpath("//div[@class='post_text']/p/text()").extract()
		time_pattern = re.compile("[0-9]{4}-[0-9]{2}-[0-9]{2}\s[0-9]{2}:[0-9]{2}")
			
		if(len(timee)!=0 and len(title)!=0 and len(content)!=0):
			tm = time_pattern.findall(timee[0])[0]
			item['time'] = int(time.mktime(time.strptime(tm,'%Y-%m-%d %H:%M')))
			item['title'] = title[0]
			item['url'] = response.url
			item['the_from'] = 'NetEase'
			cc=''
			if(len(content)!=0):
				for c in content:
					cc = cc+c+'\n'
			item['content'] = cc
			yield item
