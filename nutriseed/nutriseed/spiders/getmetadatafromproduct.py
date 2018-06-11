# -*- coding: utf-8 -*-
import scrapy
from nutriseed.items import NutriseedItem



class GetmetadatafromproductSpider(scrapy.Spider):
    name = 'getmetadatafromproduct'
    allowed_domains = []
    start_urls = []
    read_urls = open('getproductfromcollecturl.csv', 'r')
    for url in read_urls.readlines():
        url = url.strip()
        allowed_domains = allowed_domains = [url[4:]]
        start_urls = start_urls + [url]

    read_urls.close
    def parse(self, response):
        items = NutriseedItem()
        producturl = response.request.url
        productname = response.xpath('//h1[@itemprop="name"]/span/text()').extract()
        price =  response.xpath('//span[@class="product-price"]/text()').extract()
        invcount = response.xpath('//script/text()').re_first(r'"inventory_quantity":([\0-9]+\d)')
        prodcategory = response.xpath('//script/text()').re_first(r'"type":([\"a-z-A-Z\s]+)')
        items['productname'] = ''.join(productname).strip() if productname else None
        items['invcount'] = ''.join(invcount).strip() if invcount else None
        items['price'] = ''.join(price).strip() if price else None
        items['producturl'] = ''.join(producturl).strip() if producturl else None
        items['prodcategory'] = ''.join(prodcategory).strip() if prodcategory else None
        yield items