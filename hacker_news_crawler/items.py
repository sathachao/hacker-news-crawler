# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HackerNewsCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class News(scrapy.Item):
    url = scrapy.Field()
    host = scrapy.Field()
    topic = scrapy.Field()

    pass

class Comment(scrapy.Item):
    user = scrapy.Field()

    pass