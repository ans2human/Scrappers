# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SimplipleasureItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    produrl = scrapy.Field()

class SimplipleasureItem1(scrapy.Item):
    # define the fields for your item here like:
    prodname = scrapy.Field()
    prodprice = scrapy.Field()