# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class test(scrapy.Item):
    # define the fields for your item here like:
    producturl = scrapy.Field()
    prodname = scrapy.Field()
    prodprice = scrapy.Field()