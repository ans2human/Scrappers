# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SkinnydipldItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
  
class Skinnydip2ldItem(scrapy.Item):
    # define the fields for your item here like:
    producturl = scrapy.Field()
  
class Skinnydip3ldItem(scrapy.Item):
    productname = scrapy.Field()
    price = scrapy.Field()
    producturl = scrapy.Field()
    invcount = scrapy.Field()
    prodcategory = scrapy.Field()