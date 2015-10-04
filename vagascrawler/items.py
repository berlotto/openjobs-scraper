# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VagaItem(scrapy.Item):
    link = scrapy.Field()
    body = scrapy.Field()
    datetime = scrapy.Field()
    path = scrapy.Field()
    titulo = scrapy.Field()
    empresa = scrapy.Field()
    cidade = scrapy.Field()
    categoria = scrapy.Field()
