# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UkgymsharkItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    pass
class UkgymsharkItem1(scrapy.Item):
    # define the fields for your item here like:
    produrl = scrapy.Field()
    pass
class UkgymsharkItem2(scrapy.Item):
    # define the fields for your item here like:
    producturl = scrapy.Field()
    prodname = scrapy.Field()
    prodprice = scrapy.Field()
    pass
