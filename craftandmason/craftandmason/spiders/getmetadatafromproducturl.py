import scrapy

from craftandmason.items import CraftandmasonItem

class GetmetadatafromproducturlSpider(scrapy.Spider):
    name = 'getmetadatafromproducturl'
    allowed_domains = []
    start_urls = []
    read_urls = open('producturls.csv', 'r')
    for url in read_urls.readlines():
        url = url.strip() 
        allowed_domains = allowed_domains + [url[4:]]
        start_urls = start_urls + [url]
    read_urls.close()

    def parse(self, response):
        items = CraftandmasonItem()
        producturl = response.request.url
        prodname = response.xpath('//h1[@class="title"]/text()').extract()
        prodprice =  response.xpath('//div[@class="purchase"]/h2/text()').extract()

        items['prodname'] = ''.join(prodname).strip() if prodname else None
        items['producturl'] = ''.join(producturl).strip() if producturl else None
        items['prodprice'] = ''.join(prodprice).strip() if prodprice else None

        yield items
