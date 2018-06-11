# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Rvca4Item(scrapy.Item):
    # define the fields for your item here like:
    prodname = scrapy.Field()
    productid = scrapy.Field()
    prodcategory = scrapy.Field()
    prodprice = scrapy.Field()
    colors = scrapy.Field()
    quantity = scrapy.Field()
    produrl = scrapy.Field()


class CollectUrlItem(scrapy.Item):
    url = scrapy.Field()


class Stage2(scrapy.Item):
    stage2url = scrapy.Field()



