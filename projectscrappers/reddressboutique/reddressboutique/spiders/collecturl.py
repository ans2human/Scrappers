# -*- coding: utf-8 -*-
import scrapy
from reddressboutique.items import ReddressboutiqueItem

class CollecturlSpider(scrapy.Spider):
    name = 'collecturl'
    allowed_domains = ['www.reddressboutique.com']
    start_urls = ['http://www.reddressboutique.com/']


    def parse(self, response):
        items = ReddressboutiqueItem()
        for href in response.xpath('//h3/a/@href'):
            
            items['url'] = response.urljoin(href.extract())

            yield items        
