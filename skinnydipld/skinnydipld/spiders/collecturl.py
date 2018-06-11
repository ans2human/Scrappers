# -*- coding: utf-8 -*-
import scrapy
from skinnydipld.items import SkinnydipldItem

class CollecturlSpider(scrapy.Spider):
    name = 'collecturl'
    allowed_domains = ['skinnydiplondon.com']
    start_urls = ['https://www.skinnydiplondon.com/#!']

    def parse(self, response):
        items = SkinnydipldItem()
        for href in  response.xpath('//div[@class="sub-nav__menu"]/a/@href'):
            items['url'] = response.urljoin(href.extract())
            yield items