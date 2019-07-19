import scrapy,re
from urllib.parse import urljoin
from fang.items import NewHouseItem,ESFHouseItem
from scrapy_redis.spiders import RedisSpider

class FangtianxiaSpider(RedisSpider):
    name = 'fang'
    allowed_domains = ['fang.com']
    # start_urls = ['http://www.fang.com/SoufunFamily.htm']
    redis_key = "fangtianxia:start_urls"

    def parse(self, response):
        trs = response.xpath('//div[@class="outCont"]//tr')
        province = None
        for tr in trs:
            tds = tr.xpath('.//td[not(@class)]')
            province_td = tds[0]
            province_text = province_td.xpath('.//text()').extract_first()
            province_text = re.sub(r'\s','',province_text)
            if province_text:
                province = province_text
            if '其它' in province:
                continue
                
            city_links = tds[1].xpath('.//a')
            for city_link in city_links:
                city_url = city_link.xpath('.//@href').extract_first()      #'http://gz.fang.com/'
                city_name = city_link.xpath('.//text()').extract_first()    #'广州'
                url_module = city_url.split('fang')
                prefix = url_module[0]
                if 'gz' in prefix:
                    newhouse_url = 'https://newhouse.fang.com/house/s/b91/'
                    esf_url = 'https://esf.fang.com/house/i31/'
                else:
                    newhouse_url = prefix + 'newhouse.fang.com/house/s/b91/'
                    esf_url = prefix + 'esf.fang.com/house/i31/'
                    
                yield scrapy.Request(url=newhouse_url,callback=self.parse_newhouse,meta={'info':(province,city_name)})
                yield scrapy.Request(url=esf_url,callback=self.parse_esf,meta={'info':(province,city_name)})


    def parse_newhouse(self,response):
        province,city_name = response.meta.get('info')
        lis = response.xpath('//div[@class="nl_con clearfix"]/ul/li')
        for li in lis:
            ad = li.xpath('./div[@class="clearfix"]/h3/text()').extract_first()
            if ad:
                continue
            house_name = li.xpath('.//div[@class="house_value clearfix"]//div[@class="nlcd_name"]/a/text()').extract_first()
            
            if house_name:
                house_name = re.sub(r"\s","",house_name)
            
            rooms = '/'.join(li.xpath('.//div[@class="house_type clearfix"]/a/text()').extract())
            phone_num = ''.join(li.xpath('.//div[@class="tel"]/p//text()').extract())
            area = ''.join(li.xpath('.//div[@class="house_type clearfix"]/text()').extract())
            area = re.sub('\s|－|/','',area)
            address = li.xpath('.//div[@class="address"]/a/@title').extract_first()
            sale = li.xpath(".//div[@class='fangyuan']/span/text()").extract_first()
            tags_list = li.xpath('//div[@id="sjina_C26_07"]//text()').extract()
            tags = list(filter(None,map(lambda x:x.strip(),tags_list)))[1:]
            tags = '/'.join(tags)
            price = li.xpath(".//div[@class='nhouse_price']/span/text()").extract_first()
            price_unit = li.xpath(".//div[@class='nhouse_price']/em/text()").extract_first()
            nearby = li.xpath('//div[@class="nhouse_price"]/label[2]/text()').extract_first()

            if nearby:
                price = li.xpath('//div[@class="nhouse_price"]/i/text()').extract_first()
            if not price_unit:
                price = price
            else:
                price = price + price_unit      #'40500元/㎡'

            origin_url = li.xpath(".//div[@class='nlcd_name']/a/@href").extract_first()
            # 详情页可能会取空，加一个判断    TypeError: must be str, not NoneType
            if origin_url:
                origin_url = 'https:' + origin_url
            item = NewHouseItem()
            item['province'] = province
            item['city'] = city_name
            item['house_name'] = house_name
            item['sale'] = sale
            item['phone_num'] = phone_num  if phone_num else '暂无电话'
            item['price'] = price
            item['tags'] = tags
            item['rooms'] = rooms
            item['area'] = area
            item['address'] = address
            item['origin_url'] = origin_url

            yield item

            last_url = response.xpath('//ul[@class="clearfix"]/li[@class="fr"]/a[@class="last"]/@href').extract_first()     # '/house/s/b924/'
       
            if last_url:
                last_page = last_url.split('/')[-2].replace('b9','')
                for i in range(1,int(last_page)+1):
                    next_url = urljoin(response.url,'/house/s/b9{page}/'.format(page=i))
                    if next_url:
                        yield scrapy.Request(url=next_url,
                                             callback=self.parse_newhouse,
                                             meta={'info': (province, city_name)}
                                             )

    def parse_esf(self, response):
        province, city_name = response.meta.get('info')
        dls = response.xpath("//div[@class='shop_list shop_list_4']/dl")
        for dl in dls:
            item = ESFHouseItem()
            house_title = dl.xpath('//h4[@class="clearfix"]/a/@title').extract_first()

            if house_title:
                infos = dl.xpath(".//p[@class='tel_shop']/text()").extract()
                infos = list(map(lambda x: re.sub(r"\s", "", x), infos))
                for info in infos:
                    if "厅" in info:
                        item["rooms"] = info
                    elif '层' in info:
                        item["floor"] = info
                    elif '向' in info:
                        item['toward'] = info
                    elif '㎡' in info:
                        item['area'] = info
                    elif '年建' in info:
                        item['build_year'] = re.sub("年建", "", info)

             
                item['province'] = province
                item['city'] = city_name
                item['house_title'] = house_title
                item['house_name'] = dl.xpath('.//p[@class="add_shop"]/a/@title').extract_first()
                item['contacts'] = dl.xpath('.//p[@class="tel_shop"]/span[@class="people_name"]/a/text()').extract_first() if dl.xpath('.//p[@class="tel_shop"]/span[@class="people_name"]/a/text()') else '暂无联系人'
                item['address'] = dl.xpath('.//p[@class="add_shop"]/span/text()').extract_first()
                item['tags'] = '/'.join(dl.xpath('.//dd/p[3]/span/text()').extract()) if response.xpath('.//dd/p[3]/span/text()') else '暂无卖点'
                price = dl.xpath('//dd[@class="price_right"]/span[1]/b/text()').extract_first()
                price_unit = dl.xpath('//dd[@class="price_right"]/span[1]/text()').extract_first()
                item['price'] = price + price_unit
                item['unit'] = dl.xpath(".//dd[@class='price_right']/span[2]/text()").extract_first()
                detail_url = dl.xpath(".//h4[@class='clearfix']/a/@href").extract_first()
                item['origin_url'] = response.urljoin(detail_url)
                yield item
                
        last_url = response.xpath('//div[@class="page_al"]/p/a[contains(.,"末页")]/@href').extract_first()    # '/house/i3100/'
  
        if last_url:
            last_page = last_url.split('/')[-2].replace('i3','')
            for i in range(1,int(last_page)+1):
                next_url = urljoin(response.url,'/house/i3{page}/'.format(page=i))
                if next_url:
                    yield scrapy.Request(url=next_url,
                                         callback=self.parse_esf,
                                         meta={'info': (province, city_name)}
                                         )
