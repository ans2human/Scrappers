# -*- coding: utf-8 -*-
import scrapy
from negative.items import NegativeItem


class GetmetadatafromproductSpider(scrapy.Spider):
    name = 'getmetadatafromproduct'
    allowed_domains = []
    start_urls = []
    # read_urls = open('getproductsfromcollectedurls.csv', 'r')
    # for url in read_urls.readlines():
    #     url = url.strip() 
    #     allowed_domains = allowed_domains + [url[4:]]
    #     start_urls = start_urls + [url]
    # read_urls.close()
    def parse(self, response):
        
# -*- coding: utf-8 -*-


        items = NegativeItem()
        prodname = response.xpath('//h1/text()').extract_first()
        productid = response.xpath('//script/text()').re_first(r'"sku":"(\w+)"')
        prodcategory = response.xpath('//ul[@class="guide"]/li/@data-category-path').extract_first()
        prodprice = response.xpath('//span[@itemprop="price"]//text()').extract_first()
        colors = response.xpath('//script/text()').re_first(r'"color":"(\w+)"')
        quantity = response.xpath('//script/text()').re_first(r'"quantity":"(\d+)"')
        rurls = response.request.url


# response.xpath('//script[contains(text(),"name")]/text()').re_first(r'"name":"([a-zA-Z0-9\s ]+)"')
# response.xpath('//script[contains(text(),"price")]/text()').re_first(r'"price":([a-zA-Z0-9 ]+)')
# response.xpath('//script[contains(text(),"category_path")]/text()').re_first(r'"category_path":\[([^\]]+)\]')
# response.xpath('//script[contains(text(),"colors")]/text()').re(r'"colors":\[([^\]]+)\]')



        items['prodname'] = ''.join(prodname).strip() if prodname else None
        items['productid'] = ''.join(productid).strip() if productid else None
        items['prodcategory'] = ''.join(prodcategory).strip() if prodcategory else None
        items['prodprice'] = ''.join(prodprice).strip() if prodprice else None
        items['colors'] = ''.join(colors).strip() if colors else None
        items['quantity'] = ''.join(quantity).strip() if quantity else None
        items['rurls'] = ''.join(rurls).strip() if rurls else None


        yield items