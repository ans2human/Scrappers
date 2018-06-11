# -*- coding: utf-8 -*-
from pymongo import MongoClient
import scrapy
from negative.items import NegativeItem
from negative import settings

class GetproductfromcollecturlSpider(scrapy.Spider):

    name = 'getproductfromcollecturl'
    def __init__(self):
        self.db = MongoClient()
        self.start_urls = self.db.negativeunder.negcollecturls.find({}) #use appropriate finding criteria here according to the structure of data resides in that collection

    def parse(self, response):
        # other codes
        for  url in self.start_urls:
            
            items = NegativeItem()
            url = response.xpath('//a[@class="product-image"]/@href').extract()

            items['url'] = response.urljoin(url)
            yield items