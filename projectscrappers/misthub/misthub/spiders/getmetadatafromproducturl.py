import scrapy
from misthub.items import MisthubItem1

class GetproductsfromcollecturlSpider(scrapy.Spider):
    name = 'getmetadatafromproducturl'
    allowed_domains = ['colourpop.com']
    start_urls = []
    read_urls = open('producturls.csv', 'r')
    for url in read_urls.readlines():
        url = url.strip() 
        allowed_domains = allowed_domains + [url[4:]]
        start_urls = start_urls + [url]
    read_urls.close()


    def parse(self, response):
        items = MisthubItem1()
        prodname = response.xpath('//div[@class="product-info__title"]/h2/text()').extract()
        prodprice =  response.xpath('//span[@class="price-box__new"]/text()').extract()

        items['prodname'] = ''.join(prodname).strip() if prodname else None

        items['prodprice'] = ''.join(prodprice).strip() if prodprice else None

        yield items
