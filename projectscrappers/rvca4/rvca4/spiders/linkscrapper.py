# -*- coding: utf-8 -*-
import scrapy

from rvca4.items import CollectUrlItem



class LinkscrapperSpider(scrapy.Spider):
    name = 'linkscrapper'
    allowed_domains = ['rvca.com']
    start_urls = ['http://rvca.com/']




    def parse(self, response):
        items = CollectUrlItem()
        for href in response.xpath('//ul[@class="level2 unstyled"]/li/a/@href'):
            items['url'] = response.urljoin(href.extract())
            yield items



