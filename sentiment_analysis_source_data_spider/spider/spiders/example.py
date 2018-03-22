# -*- coding: utf-8 -*-
import scrapy
from Test.items import TestItem
# from Test.items import addEntry


class ExampleSpider(scrapy.Spider):
    name = 'example'#爬虫名称
    allowed_domains = ['douban.com']
    start_urls = ['http://tieba.baidu.com/']

        #重写start_requests
    # urls=['https://github.com/explore']
    #
    # #重写start_requests,使用我们自己的urls变量作为其实url
    # def start_requests(self):
    #     for url in self.urls:
    #         yield self.make_requests_from_url(url)


            #重写构造函数，传参
    #可以通过-a选项传参
    #scrapy crawl -a myurl="http://www.dytt8.net/html/gndy/dyzz/20171014/55296.html" example --nolog
    def __init__(self,myurl=None,*args,**kwargs):
        super(ExampleSpider,self).__init__(*args,**kwargs)
        print("要爬取的网址为%s"%myurl)
        #重新定义start_urls
        self.start_urls=["%s"%myurl]


    def parse(self, response):
        """处理响应的默认方法"""
        item=TestItem()
        item['urlname']=response.xpath('/html/head/title/text()')
        print(item['urlname'])
        print('fsdgf')


