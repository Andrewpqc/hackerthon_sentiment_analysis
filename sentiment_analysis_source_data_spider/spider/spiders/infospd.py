# -*- coding: utf-8 -*-
import scrapy
import re
from Test.items import TestItem

import json
from scrapy.http  import Request
with open('/home/lenovo/桌面/PythonEx/Test/Test/spiders/data.json','r') as f:
    movieIds=json.loads(f.read())



class InfospdSpider(scrapy.Spider):
    name = 'infospd'
    allowed_domains = ['douban.com']
    #'https://movie.douban.com/subject/1295644/comments?start=41&limit=20&sort=new_score&status=P'
    start_urls = ['https://movie.douban.com/subject/1292052/comments?start=0&limit=20&sort=new_score&status=P']
    #https:\ / \ / movie.douban.com\ / subject\ / 1292052\ /
    def parse(self, response):
        mid=response.url.split('/')[-2]
        print("当前的电影ID:",movieIds.index(mid))
        cid=response.url.split('?')[-1].split('&')[0].split('=')[-1]
        print("当前的评论起始ID:",cid)
        item=TestItem()
        item['comment']=response.xpath('//div[@class="comment-item"]/div[@class="comment"]/p/text()').extract()
        yield item

        for id in movieIds[1:-1]:
            for commentid in range(0,201,20):
                url='https://movie.douban.com/subject/'+str(id)+'/comments?start='+str(commentid)+'&limit=20&sort=new_score&status=P'
                yield Request(url,callback=self.parse)

