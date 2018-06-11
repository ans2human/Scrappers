# -*- coding: utf-8 -*-
import scrapy
from craftandmason.items import CraftandmasonItem

class CollecturlSpider(scrapy.Spider):
    name = 'collecturl'
    allowed_domains = ['craftandmason.com']
    start_urls = ['https://craftandmason.com/collections/current-offerings']

    def parse(self, response):
        items = CraftandmasonItem()
        for href in  response.xpath('//div[@class="details"]/a/@href'):
            items['producturl'] = response.urljoin(href.extract())
            yield items