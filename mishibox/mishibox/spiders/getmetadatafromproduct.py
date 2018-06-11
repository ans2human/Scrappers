# -*- coding: utf-8 -*-
import scrapy
from mishibox.items import MishiboxItem


class GetmetadatafromproductSpider(scrapy.Spider):
    name = 'getmetadatafromproduct'
    allowed_domains = []
    start_urls = []
    read_urls = open('producturls.csv', 'r')
    for url in read_urls.readlines():
        url = url.strip() 
        allowed_domains = allowed_domains + [url[4:]]
        start_urls = start_urls + [url]
    read_urls.close()

    def parse(self, response):
        items = MishiboxItem()
        producturl = response.request.url
        price = response.xpath('//p[@class="modal_price"]//span[@class="money"]/text()').extract_first()
        productname =  response.xpath('//h1[@class="product_name"]/text()').extract()
        invcount = response.xpath('//script[@data-app="esc-out-of-stock"]/text()').re_first(r'"inventory_quantity":([{a-zA-Z0-9]+)')
        productcolor = response.xpath('//div[@class="select"]//option[@selected="selected"]/text()').extract_first()
        prodcategory = response.xpath('//p/span[@itemprop="category"]/a/@href').extract()
        items['productname'] = ''.join(productname).strip() if productname else None
        items['price'] = ''.join(price).strip() if price else None        
        items['invcount'] = ''.join(invcount).strip() if invcount else None
        items['producturl'] = ''.join(producturl).strip() if producturl else None
        items['productcolor'] = ''.join(productcolor).strip() if productcolor else None
        items['prodcategory'] = ''.join(prodcategory).strip() if prodcategory else None

        yield items