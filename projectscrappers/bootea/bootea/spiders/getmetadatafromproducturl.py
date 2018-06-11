import scrapy
from bootea.items import test


class GetproductsfromcollecturlSpider(scrapy.Spider):
    name = 'getmetadatafromproducturl'
    allowed_domains = []
    start_urls = []
    read_urls = open('collecturls.csv', 'r')
    for url in read_urls.readlines():
        url = url.strip() 
        allowed_domains = allowed_domains + [url[4:]]
        start_urls = start_urls + [url]
    read_urls.close()




    def parse(self, response):
        items = test()
        producturl = response.request.url
        prodname = response.xpath('//h1[@class="prod-title"]/text()').extract()
        prodprice =  response.xpath('//span[@class="product-price h2 desktop-hide"]/text()').extract()

        items['prodname'] = ''.join(prodname).strip() if prodname else None

        items['prodprice'] = ''.join(prodprice).strip() if prodprice else None

        items['producturl'] = ''.join(producturl).strip() if producturl else None

        yield items
