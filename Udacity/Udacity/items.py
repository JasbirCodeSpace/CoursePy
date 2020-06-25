# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UdacityItem(scrapy.Item):
    name = scrapy.Field()
    category = scrapy.Field()
    difficulty = scrapy.Field()
    link = scrapy.Field()
    image = scrapy.Field()
