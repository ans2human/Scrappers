# -*- coding: utf-8 -*-
import scrapy
from negative.items import NegativeItem


class CollecturlSpider(scrapy.Spider):
    name = 'collecturl'
    allowed_domains = ['www.negativeunderwear.com']
    start_urls = ['http://www.negativeunderwear.com/']

    def parse(self, response):
        items = NegativeItem()
        for href in response.xpath('//li[@class="mobile-nav__item"]/a/@href'):
            items['url'] = response.urljoin(href.extract())
            yield items

