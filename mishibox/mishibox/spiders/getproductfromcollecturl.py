# # -*- coding: utf-8 -*-
# import scrapy
# from mishibox.items import MishiboxItem


# class GetproductfromcollecturlSpider(scrapy.Spider):
#     name = 'getproductfromcollecturl'
#     allowed_domains = ['www.mishibox.com']
#     start_urls = ['https://www.mishibox.com/collections/all-products']

#     def parse(self, response):
#         items = MishiboxItem()
#         produrl = response.xpath('//div[@class="three columns alpha thumbnail even"]/a/@href').extract()
#         produrl1 = response.xpath('//div[@class="three columns omega thumbnail odd"]/a/@href').extract()
#         produrl2 = response.xpath('//div[@class="three columns  thumbnail odd"]/a/@href').extract()
#         produrl3 = response.xpath('//div[@class="three columns  thumbnail even"]/a/@href').extract()
#         items['produrl'] = ''.join(produrl).strip() if produrl else None
#         items['produrl1'] = ''.join(produrl1).strip() if produrl1 else None
#         items['produrl2'] = ''.join(produrl2).strip() if produrl2 else None
#         items['produrl3'] = ''.join(produrl3).strip() if produrl3 else None

#         yield items        
