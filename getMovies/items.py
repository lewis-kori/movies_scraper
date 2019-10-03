# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item
class GetmoviesItem(scrapy.Item):
    # define the fields for your item here like:
    title=scrapy.Field()
    rating=scrapy.Field()
    description=scrapy.Field()
    poster_link=scrapy.Field()
    
