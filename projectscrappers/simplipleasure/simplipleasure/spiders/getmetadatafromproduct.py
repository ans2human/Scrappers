# -*- coding: utf-8 -*-
import scrapy
from simplipleasure.items import SimplipleasureItem1


class GetmetadatafromproductSpider(scrapy.Spider):
    name = 'getmetadatafromproduct'
    allowed_domains = []
    start_urls = []
    read_urls = open('producturls.csv', 'r')
    for url in read_urls.readlines():
        url = url.strip()
        allowed_domains = allowed_domains = [url[4:]]
        start_urls = start_urls + [url]

    read_urls.close
    def parse(self, response):
        items = SimplipleasureItem1()
        prodname = response.xpath('//h1[@itemprop="name"]/text()').extract()
        prodprice = response.xpath('//span[@class="current_price"]/text()').extract()

        items['prodname'] = ''.join(prodname).strip() if prodname else None

        items['prodprice'] = ''.join(prodprice).strip() if prodprice else None

        yield items