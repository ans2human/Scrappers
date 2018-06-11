# -*- coding: utf-8 -*-
import scrapy
from skinnymetea.items import SkinnymeteaItem1


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
        items = SkinnymeteaItem1()
        for href in response.xpath('//div[@class="figcaption under text-center"]/a/@href'):
            
            items['produrl'] = response.urljoin(href.extract())

            yield items        
