# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class CourseraItem(scrapy.Item):
    name = scrapy.Field()
    image = scrapy.Field()
    category = scrapy.Field()
    rating = scrapy.Field()
    enrollment = scrapy.Field()
    university = scrapy.Field()
    difficulty = scrapy.Field()
    link = scrapy.Field()

