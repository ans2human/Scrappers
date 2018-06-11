# -*- coding: utf-8 -*-
import scrapy
from nutriseed.items import NutriseedItem


class GetproductfromcollecturlSpider(scrapy.Spider):
    name = 'getproductfromcollecturl'
    allowed_domains = []
    start_urls = []
    read_urls = open('collecturl.csv', 'r')
    for url in read_urls.readlines():
        url = url.strip()
        allowed_domains = allowed_domains = [url[4:]]
        start_urls = start_urls + [url]

    read_urls.close


    def parse(self, response):
        item = NutriseedItem()
        for href in response.xpath('//div[@id="product-info"]/a/@href'):
            item['producturl'] = response.urljoin(href.extract())
            yield item


