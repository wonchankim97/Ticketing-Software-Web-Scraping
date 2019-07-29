# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CapterraItem(scrapy.Item):
    name = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    position = scrapy.Field()
    industry = scrapy.Field()
    usage = scrapy.Field()
    paid = scrapy.Field()
    
    overall = scrapy.Field()
    ease = scrapy.Field()
    support = scrapy.Field()
    features = scrapy.Field()
    value = scrapy.Field()
    meter = scrapy.Field()
    
    pro = scrapy.Field()
    con = scrapy.Field()
    review = scrapy.Field()