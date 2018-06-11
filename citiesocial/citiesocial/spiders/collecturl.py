# -*- coding: utf-8 -*-
import scrapy
from citiesocial.items import CitiesocialItem

class CollecturlSpider(scrapy.Spider):
    name = 'collecturl'
    allowed_domains = ['citiesocial.com']
    start_urls = ['https://www.citiesocial.com']

    def parse(self, response):
        items = CitiesocialItem()
        for href in  response.xpath('//li/a/@href'):
            items['url'] = response.urljoin(href.extract())
            yield items