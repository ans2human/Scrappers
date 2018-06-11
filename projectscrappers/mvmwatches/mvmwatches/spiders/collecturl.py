# -*- coding: utf-8 -*-
import scrapy
from mvmwatches.items import MvmwatchesItem

class CollecturlSpider(scrapy.Spider):
    name = 'collecturl'
    allowed_domains = ['mvmtwatches.com']
    start_urls = ['https://www.mvmtwatches.com/collections/best-sellers/']

    def parse(self, response):
        items = MvmwatchesItem()
        for href in response.xpath('//a[@class="prod-grid-image-link"]/@href'):
            items['url'] = response.urljoin(href.extract())
            yield items
