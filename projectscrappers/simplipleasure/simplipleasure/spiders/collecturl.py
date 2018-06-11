# -*- coding: utf-8 -*-
import scrapy
from simplipleasure.items import SimplipleasureItem

class CollecturlSpider(scrapy.Spider):
    name = 'collecturl'
    allowed_domains = ['simplipleasure.com']
    start_urls = ['https://www.simplipleasure.com/']

    def parse(self, response):
        items = SimplipleasureItem()
        for href in response.xpath('//li/a/@href'):
            
            items['url'] = response.urljoin(href.extract())

            yield items        
