# -*- coding: utf-8 -*-
import scrapy
from fashionnova.items import FashionnovaItem

class CollecturlSpider(scrapy.Spider):
    name = 'collecturl'
    allowed_domains = ['www.fashionnova.com']
    start_urls = ['http://www.fashionnova.com/']

    def parse(self, response):
        items = FashionnovaItem()
        for href in response.xpath('//li/a/@href'):
            
            items['url'] = response.urljoin(href.extract())

            yield items        
