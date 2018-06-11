# -*- coding: utf-8 -*-
import scrapy
from reddressboutique.items import ReddressboutiqueItem1


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
        items = ReddressboutiqueItem1()
        producturl = response.request.url
        productname = response.xpath('//h1[@class="product_title"]/text()').extract()
        price =   response.xpath('//h5[@class="price"]/text()').extract()
        invcount = response.xpath('//script[@id="back-in-stock-helper"]/text()').re_first(r'"inventory_quantity":([\d]+)')
        prodcategory = response.xpath('//script[@class="analytics"]/text()').re(r'"category":([\"a-zA-Z]+)')
        productcolor = response.xpath('//div[@class="options colors color_radios_group hide"]//@value').extract()
        productsizes = response.xpath('//script[@id="back-in-stock-helper"]/text()').re(r'"option1":([\."a-z-A-Z0-9]+)')
        items['producturl'] = ''.join(producturl).strip() if producturl else None
        items['productname'] = ''.join(productname).strip() if productname else None
        items['price'] = ''.join(price).strip() if price else None
        items['invcount'] = ''.join(invcount).strip() if invcount else None
        items['prodcategory'] = ''.join(prodcategory).strip() if prodcategory else None
        items['productcolor'] = ''.join(productcolor).strip() if productcolor else None
        items['productsizes'] = ''.join(productsizes).strip() if productsizes else None

        yield items