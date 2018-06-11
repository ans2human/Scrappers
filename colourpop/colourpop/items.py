# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ColourpopItem(scrapy.Item):
    produrl = scrapy.Field()
    prodname = scrapy.Field()
    prodprice = scrapy.Field()
    pass
