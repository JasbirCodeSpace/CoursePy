# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PluralsightItem(scrapy.Item):
    name = scrapy.Field()
    category = scrapy.Field()
    rating = scrapy.Field()
    author = scrapy.Field()
    difficulty = scrapy.Field()
    duration = scrapy.Field()
    link = scrapy.Field()
