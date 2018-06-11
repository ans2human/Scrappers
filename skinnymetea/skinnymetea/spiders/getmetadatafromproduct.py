# -*- coding: utf-8 -*-
import scrapy
from skinnymetea.items import SkinnymeteaItem2

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
        items = SkinnymeteaItem2()
        producturl = response.request.url
        productname = response.xpath('//h1[@itemprop="name"]/text()').extract()
        price = response.xpath('//span[@id="ProductPrice-product"]//text()').extract()
        prodcategory = response.xpath('//script[@id="ProductJson-product"]/text()').re(r'"tags":([\a-zA-Z]+])')
        invcount = response.xpath('//script[@id="ProductJson-product"]/text()').re(r'"inventory_quantity":([\0-9]+\d)')


        items['producturl'] = ''.join(producturl).strip() if producturl else None
        items['productname'] = ''.join(productname).strip() if productname else None
        items['price'] = ''.join(price).strip() if price else None
        items['prodcategory'] = ''.join(prodcategory).strip() if prodcategory else None
        items['invcount'] = ''.join(invcount).strip() if invcount else None

        yield items