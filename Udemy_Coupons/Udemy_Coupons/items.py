# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UdemyCouponsItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    tags = scrapy.Field()
    link = scrapy.Field()
    code = scrapy.Field()
