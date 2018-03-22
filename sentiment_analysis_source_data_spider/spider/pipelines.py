# -*- coding: utf-8 -*-
from pprint import pprint
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from Test.database import addEntry

class TestPipeline(object):
    def __int__(self):
        """做初始化工作，如打开文件"""
        pass

    def process_item(self, item, spider):
        """实际操作，如将数据存入文件"""
        addEntry(item['comment'])
        return item

    def close_spider(self,spider):
        """做收尾工作，如关闭刚才打开额文件"""
        pass