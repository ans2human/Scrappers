# -*- coding: utf-8 -*-
import scrapy
from ukgymshark.items import UkgymsharkItem

class CollecturlSpider(scrapy.Spider):
    name = 'collecturl'
    allowed_domains = ['row.gymshark.com']
    start_urls = ['http://row.gymshark.com/']

    def parse(self, response):
        items = UkgymsharkItem()
        for href in response.xpath('//ul[@class="subsub"]/li/a/@href'):
            
            items['url'] = response.urljoin(href.extract())

            yield items        
