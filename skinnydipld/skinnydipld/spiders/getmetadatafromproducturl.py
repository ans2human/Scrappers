import scrapy
from skinnydipld.items import Skinnydip3ldItem

class getmetadatafromproducturlSpider(scrapy.Spider):
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
        items = Skinnydip3ldItem()
        producturl = response.request.url
        productname = response.xpath('//h1[@itemprop="name"]/text()').extract()
        price = response.xpath('//span[@class="money"]/text()').extract_first()
        invcount = response.xpath('//script/text()').re(r'"inventory_quantity":([\0-9]+\d)')
        prodcategory = response.xpath('//script/text()').re(r'"tags":([\a-zA-Z]+])')

        items['invcount'] = ''.join(invcount).strip() if invcount else None
        items['productname'] = ''.join(productname).strip() if productname else None
        items['price'] = ''.join(price).strip() if price else None
        items['prodcategory'] = ''.join(prodcategory).strip() if prodcategory else None
        items['producturl'] = ''.join(producturl).strip() if producturl else None
        

        yield items