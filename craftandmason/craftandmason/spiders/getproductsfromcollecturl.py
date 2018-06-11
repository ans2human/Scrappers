# #-*- coding: utf-8 -*-
# import scrapy

# from craftandmason.items import CraftandmasonItem


# class GetproductsfromcollecturlSpider(scrapy.Spider):
#     name = 'getproductsfromcollecturl'
#     allowed_domains = []
#     start_urls = []
#     read_urls = open('collecturls.csv', 'r')
#     for url in read_urls.readlines():
#         url = url.strip() 
#         allowed_domains = allowed_domains + [url[4:]]
#         start_urls = start_urls + [url]
#     read_urls.close()



#     def parse(self, response):
#         items = Skinnydip2ldItem()
#         for href in  response.xpath('//div[@class="details"]/a/@href'):
#             items['produrl'] = response.urljoin(href.extract())
#             yield items
