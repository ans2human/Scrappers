import scrapy
import logging


#from rvca4.items import CollectUrlItem

class Stage2Spider(scrapy.Spider):
    name = 'stage2'
    allowed_domains = []
    start_urls = []
    read_urls = open('collecturls.csv', 'r')
    for url in read_urls.readlines():
        url = url.strip() 
        allowed_domains = allowed_domains + [url[4:]]
        start_urls = start_urls + [url]
    read_urls.close()





    def parse(self, response):
        #items = CollectUrlItem()
        for href in response.xpath('//a[@class="product-image"]/@href'):
            items['stage2url'] = response.urljoin(href.extract())
            yield items
