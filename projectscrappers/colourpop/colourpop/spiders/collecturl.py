# -*- coding: utf-8 -*-
import scrapy
from colourpop.items import ColourpopItem


class CollecturlSpider(scrapy.Spider):
    name = 'collecturl'
    allowed_domains = ['colourpop.com']
    start_urls = ['https://colourpop.com']

    def parse(self, response):     
        items = ColourpopItem()
        for href in  response.xpath('//div/a/@href'):     
            items['produrl'] = response.urljoin(href.extract())
            yield items

