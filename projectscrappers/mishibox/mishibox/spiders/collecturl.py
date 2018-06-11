# # -*- coding: utf-8 -*-
# import scrapy
# from mishibox.items import MishiboxItem

# class CollecturlSpider(scrapy.Spider):
#     name = 'collecturl'
#     allowed_domains = ['www.mishibox.com']
#     start_urls = ['http://www.mishibox.com/']

#     def parse(self, response):
#         items = MishiboxItem()
#         for href in response.xpath('//ul[@class="animated fadeIn"]/li/a/@href'):
            
#             items['url'] = response.urljoin(href.extract())

#             yield items        
