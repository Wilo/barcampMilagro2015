# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class PushfeedItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    description = Field()
    link = Field()
    img  = Field()
    date = Field()
