# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule 
from scrapy.linkextractors import LinkExtractor
from skinnydipld.items import Skinnydip2ldItem

class GetproductsfromcollecturlSpider(CrawlSpider):
    name = 'getproductsfromcollecturl'
    allowed_domains = []
    start_urls = []
    read_urls = open('collecturls.csv', 'r')
    for url in read_urls.readlines():
        url = url.strip() 
        allowed_domains = allowed_domains + [url[4:]]
        start_urls = start_urls + [url]
    read_urls.close()

    # rules = (
    #         rule(linkextractor(allow = (),
    #             restrict_xpaths=('//span[@class="next"]')),
    #             callback='parse',
    #             follow=true),
    #         )

    #rules = (Rule(LinkExtractor(allow=()), callback='parse', follow=True),)

    def parse(self, response):
        item = Skinnydip2ldItem()
        for href in response.xpath('//div[@class="reveal"]/a/@href'):
            item['produrl'] =  response.urljoin(href.extract())
            yield item
            
