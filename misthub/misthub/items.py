# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MisthubItem(scrapy.Item):
    # define the fields for your item here like:
    produrl = scrapy.Field()

class MisthubItem1(scrapy.Item):
    prodname = scrapy.Field()
    prodprice = scrapy.Field()