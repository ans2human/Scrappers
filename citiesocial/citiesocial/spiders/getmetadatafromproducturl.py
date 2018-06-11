import scrapy

from citiesocial.items import CitiesocialItem1

class GetproductsfromcollecturlSpider(scrapy.Spider):
    name = 'getmetadatafromproducturl'
    allowed_domains = []
    start_urls = []
    read_urls = open('producturl.csv', 'r')
    for url in read_urls.readlines():
        url = url.strip() 
        allowed_domains = allowed_domains + [url[4:]]
        start_urls = start_urls + [url]
    read_urls.close()



    def parse(self, response):
        items = CitiesocialItem1()
        prodname =  response.xpath('//h1[@class="product-meta__title"]/text()').extract()
        prodprice =  response.xpath('//div[@class="product-meta__prices"]/span/text()').extract()
        items['prodname'] = ''.join(prodname).strip() if prodname else None

        items['prodprice'] = ''.join(prodprice).strip() if prodprice else None

        yield items
