# -*- coding: utf-8 -*-
import scrapy
from misthub.items import MisthubItem

class CollecturlSpider(scrapy.Spider):
    name = 'collecturl'
    allowed_domains = ['misthub.com']
    start_urls = ['https://www.misthub.com/']

    def parse(self, response):
        items = MisthubItem()
        for href in response.xpath('//li[@class="level2"]/a/@href'):
            items['url'] = response.urljoin(href.extract())
            yield items

            