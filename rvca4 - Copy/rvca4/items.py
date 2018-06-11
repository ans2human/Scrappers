# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class products(scrapy.Item):
    # define the fields for your item here like:
    productname = scrapy.Field()
    prodcategory = scrapy.Field()
    price = scrapy.Field()
    productcolor = scrapy.Field()
    invcount = scrapy.Field()
    producturl = scrapy.Field()


# class CollectUrlItem(scrapy.Item):
#     stage2url = scrapy.Field()


# class Stage2(scrapy.Item):
#     stage2url = scrapy.Field()



