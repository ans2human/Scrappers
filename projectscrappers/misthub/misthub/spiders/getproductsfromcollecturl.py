#-*- coding: utf-8 -*-
import scrapy

from misthub.items import MisthubItem


class GetproductsfromcollecturlSpider(scrapy.Spider):
    name = 'getproductsfromcollecturl'
    allowed_domains = []
    start_urls = []
    read_urls = open('collecturl.csv', 'r')
    for url in read_urls.readlines():
        url = url.strip() 
        allowed_domains = allowed_domains + [url[4:]]
        start_urls = start_urls + [url]
    read_urls.close()



    def parse(self, response):
        items = MisthubItem()
        for href in  response.xpath('//h3[@class="product_title"]/a/@href'):
            items['produrl'] = response.urljoin(href.extract())
            yield items
