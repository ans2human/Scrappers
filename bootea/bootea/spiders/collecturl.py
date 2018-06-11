# import scrapy
# from bootea.items import BooteaItem

# class CollecturlSpider(scrapy.Spider):
#     name = 'collecturl'
#     allowed_domains = ['bootea.com']
#     start_urls = ['https://us.bootea.com/collections/all']

#     def parse(self, response):
#         items = BooteaItem()
#         for href in response.xpath('//p[@class="h4 loop-title"]//a/@href'):
#             items['producturl'] = response.urljoin(href.extract())
#             yield items

            