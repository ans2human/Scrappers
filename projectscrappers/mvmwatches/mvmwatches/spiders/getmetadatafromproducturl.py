import scrapy

from colourpop.items import ColourpopItem

class GetproductsfromcollecturlSpider(scrapy.Spider):
    name = 'getmetadatafromproducturl'
    allowed_domains = ['colourpop.com']
    start_urls = ['https://colourpop.com/products/hennyways',
                  'https://colourpop.com/products/steelo',
                  'https://colourpop.com/products/sessy',
                  'https://colourpop.com/products/nitty',
                  'https://colourpop.com/products',
                  'https://colourpop.com/products',
                  'https://colourpop.com/products',
                  'https://colourpop.com/products',
                  'https://colourpop.com/products',
                  'https://colourpop.com/products',
                  'https://colourpop.com/products',
                  'https://colourpop.com/products',
                  'https://colourpop.com/products',
                  'https://colourpop.com/products',
                  'https://colourpop.com/products',
                  'https://colourpop.com/products',
                  'https://colourpop.com/products',
                  'https://colourpop.com/products',
                  'https://colourpop.com/products',
                  'https://colourpop.com/products',
                  'https://colourpop.com/products',
                  'https://colourpop.com/products',
                  'https://colourpop.com/products',
                  'https://colourpop.com/products',
                  'https://colourpop.com/products',
                  'https://colourpop.com/products',
                  'https://colourpop.com/products']




    def parse(self, response):
        items = ColourpopItem()
        prodname = response.xpath('//h1[@class="prod-name"]/text()').extract()
        prodprice =  response.xpath('//h2[@id="mainprice"]/text()').extract()

        items['prodname'] = ''.join(prodname).strip() if prodname else None

        items['prodprice'] = ''.join(prodprice).strip() if prodprice else None

        yield items
