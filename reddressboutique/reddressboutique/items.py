# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ReddressboutiqueItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    produrl = scrapy.Field()

class ReddressboutiqueItem1(scrapy.Item):
    # define the fields for your item here like:
    productname = scrapy.Field()
    price = scrapy.Field()
    producturl = scrapy.Field()
    invcount = scrapy.Field()
    prodcategory = scrapy.Field()
    productsizes = scrapy.Field()
    productcolor = scrapy.Field()
    
