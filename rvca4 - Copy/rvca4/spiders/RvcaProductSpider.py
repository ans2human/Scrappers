#-*- coding: utf-8 -*-
import scrapy
from rvca4.items import products


class RvcaProductSpider(scrapy.Spider):
    name = 'RvcaProductSpider'
    allowed_domains = []
    start_urls = []
    read_urls = open('getproductsfromcollectedurls.csv', 'r')
    for url in read_urls.readlines():
        url = url.strip() 
        allowed_domains = allowed_domains + [url[4:]]
        start_urls = start_urls + [url]
    read_urls.close()

    def parse(self, response):
        item = products()
        productname = response.xpath('//h1[@class="product-name"]/text()').extract_first()
        #productid = response.xpath('//script/text()').re_first(r'"sku":"(\w+)"')
        prodcategory = response.xpath('//ul[@class="guide"]/li/@data-category-path').extract_first()
        price = response.xpath('//span[@itemprop="price"]//text()').extract_first()
        productcolor = response.xpath('//script/text()').re_first(r'"color":"(\w+)"')
        invcount = response.xpath('//script/text()').re_first(r'"quantity":"(\d+)"')
        producturl = response.request.url


# response.xpath('//script[contains(text(),"name")]/text()').re_first(r'"name":"([a-zA-Z0-9\s ]+)"')
# response.xpath('//script[contains(text(),"price")]/text()').re_first(r'"price":([a-zA-Z0-9 ]+)')
# response.xpath('//script[contains(text(),"category_path")]/text()').re_first(r'"category_path":\[([^\]]+)\]')
# response.xpath('//script[contains(text(),"colors")]/text()').re(r'"colors":\[([^\]]+)\]')


        item['productname'] = ''.join(productname).strip() if productname else None
        #tem['productid'] = ''.join(productid).strip() if productid else None
        item['prodcategory'] = ''.join(prodcategory).strip() if prodcategory else None
        item['price'] = ''.join(price).strip() if price else None
        item['productcolor'] = ''.join(productcolor).strip() if productcolor else None
        item['invcount'] = ''.join(invcount).strip() if invcount else None
        item['producturl'] = ''.join(producturl).strip() if producturl else None


        yield item