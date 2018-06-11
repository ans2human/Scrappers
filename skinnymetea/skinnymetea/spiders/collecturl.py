# -*- coding: utf-8 -*-
import scrapy
from skinnymetea.items import SkinnymeteaItem

class CollecturlSpider(scrapy.Spider):
    name = 'collecturl'
    allowed_domains = ['skinnymetea.com']
    start_urls = ['https://www.skinnymetea.com.au/']


    def parse(self, response):
        items = SkinnymeteaItem()
        for href in  response.xpath('//li[@class="child  kids-0"]/a/@href'):
            
            items['url'] = response.urljoin(href.extract())

            yield items        
