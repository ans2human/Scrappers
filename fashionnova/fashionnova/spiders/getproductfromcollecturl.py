# -*- coding: utf-8 -*-
import scrapy
from fashionnova.items import FashionnovaItem1


class GetproductfromcollecturlSpider(scrapy.Spider):
    name = 'getproductfromcollecturl'
    allowed_domains = []
    start_urls = []
    read_urls = open('collecturls.csv', 'r')
    for url in read_urls.readlines():
        url = url.strip()
        allowed_domains = allowed_domains = [url[4:]]
        start_urls = start_urls + [url]

    read_urls.close

    def parse(self, response):
        items = FashionnovaItem1()

        for href in  response.xpath('//a[@class="link-color-swatch"]/@href'):

            
            items['producturl'] = response.urljoin(href.extract())


            yield items        
