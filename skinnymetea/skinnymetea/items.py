# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SkinnymeteaItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()

class SkinnymeteaItem1(scrapy.Item):
    # define the fields for your item here like:
    produrl = scrapy.Field()
class SkinnymeteaItem2(scrapy.Item):
    # define the fields for your item here like:
    productname = scrapy.Field()
    invcount = scrapy.Field()
    producturl = scrapy.Field()
    prodcategory = scrapy.Field()
    price = scrapy.Field()