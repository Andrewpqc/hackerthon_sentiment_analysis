# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class TestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # movieId=scrapy.Field()
    comment=scrapy.Field()





"""
下面我们就可以这样使用了
c1=TestItem(comment="this is a comment")
print(c1)

{'comment':'this is a comment'}


"""
