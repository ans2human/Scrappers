# -*- coding: utf-8 -*-
import scrapy
from ukgymshark.items import UkgymsharkItem2


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
        items = UkgymsharkItem2()
        producturl = response.request.url
        prodname = response.xpath('//h1/text()').extract_first()
        prodprice =   response.xpath('//div[@class="info_subtext"]/span[@class="info_price"]/text()').extract()


        items['prodname'] = ''.join(prodname).strip() if prodname else None
        items['producturl'] = ''.join(producturl).strip() if producturl else None
        items['prodprice'] = ''.join(prodprice).strip() if prodprice else None

        yield items