# -*- coding: utf-8 -*-
import scrapy
import json
from time import sleep
from jobSpider.items import LagouSpiderItem
from jobSpider.settings import LAGOU_AREA_LIST, LAGOU_COMPANY_FINANCE


class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    # start_urls = ['http://lagou.com/']
    def __init__(self, keyword=None, *args, **kwargs):
        super(LagouSpider, self).__init__(*args, **kwargs)
        self.keyword = keyword

    def start_requests(self):
        for area in LAGOU_AREA_LIST:
            for finance in LAGOU_COMPANY_FINANCE:
                for pagenum in range(1, 31):
                    for i in ['true', 'false']:
                        url = 'https://www.lagou.com/jobs/positionAjax.json?jd={}&px=default&city={}&district={}&needAddtionalResult=false'.format(finance, '广州', area)
                        formdata = {
                            'first': i,
                            'pn': str(pagenum),
                            'kd': self.keyword
                        }
                        yield scrapy.FormRequest(url=url, formdata=formdata)

    def parse(self, response):
        if response.status == 200:
            data = json.loads(response.body)
            print(data)
            job_list = data['content']['positionResult']['result']
            for job in job_list:
                detail_url = 'https://www.lagou.com/jobs/{}.html'.format(job['positionId'])
                yield scrapy.Request(url=detail_url, callback=self.detail_parse)

    def detail_parse(self, response):
        item = LagouSpiderItem()
        item['company'] = response.xpath('//div[@class="company"]/text()').extract_first()
        item['job_name'] = response.xpath('//div[@class="job-name"/@title]').extract_first()
        print(item)
