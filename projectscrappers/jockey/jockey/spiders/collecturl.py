# -*- coding: utf-8 -*-
import scrapy
from jockey.items import JockeyItem

class CollecturlSpider(scrapy.Spider):
    name = 'collecturl'
    allowed_domains = ['jockey.com']
    start_urls = ['https://www.jockeyindia.com/women/products']

    def parse(self, response):
        items = JockeyItem()
        for href in  response.xpath('//div[@class="details"]/a/@href'):
            items['url'] = response.urljoin(href.extract())
            yield items