# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FashionnovaItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
 
class FashionnovaItem1(scrapy.Item):
    # define the fields for your item here like:
    producturl = scrapy.Field()
 
class FashionnovaItem2(scrapy.Item):
    # define the fields for your item here like:
    prodname = scrapy.Field()
    prodprice = scrapy.Field()
    producturl = scrapy.Field()

