# -*- coding: utf-8 -*-
import scrapy
from mvmwatches.items import MvmwatchesItem


class GetproductfromcollecturlSpider(scrapy.Spider):
    name = 'getproductfromcollecturl'
    allowed_domains = ['mvmtwatches.com']
    start_urls = ['https://www.mvmtwatches.com/collections/best-sellers/products/chrono-gun-metal-sandstone-leather']
    # read_urls = open('producturl.csv', 'r')
    # for url in read_urls.readlines():
    #     url = url.strip() 
    #     allowed_domains = allowed_domains + [url[4:]]
    #     start_urls = start_urls + [url]
    # read_urls.close()


    def parse(self, response):
        items = MvmwatchesItem()
        prodname = response.xpath('//h1[@class="product-name product-name--upsell-shown"]/text()').extract()
        items['prodname'] = ''.join(prodname).strip() if prodname else None
        yield items
