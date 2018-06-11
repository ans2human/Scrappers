# -*- coding: utf-8 -*-
import scrapy
from nutriseed.items import NutriseedItem

class CollecturlSpider(scrapy.Spider):
    name = 'collecturl'
    allowed_domains = ['www.nutriseed.co.uk']
    start_urls = ['http://www.nutriseed.co.uk']

    def parse(self, response):
        items = NutriseedItem()
        for href in response.xpath('//div[@class="submaindiv"]/li/a/@href'):
            
            items['url'] = response.urljoin(href.extract())

            yield items        
