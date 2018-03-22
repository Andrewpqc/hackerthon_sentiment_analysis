# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class TestSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

with open('//home/lenovo/桌面/PythonEx/Test/Test/ipport.txt','r') as f:
    ips=f.readlines()
# import requests
# a=requests.get('http://tvp.daxiangdaili.com/ip/?tid=559677457592481&num=1000&delay=1&category=2&protocol=https').content
# ips=a
# import threading
# import time


# time.sleep(15) # 15秒后停止定时器
# timer.cancel()
# for i in ips:
#     print(i)
#ip池
# from Test.settings import IPPOOL
# from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware
# from Test.ips import
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
import random
class IPPOOLS(HttpProxyMiddleware):
    def __init__(self,ip=''):
        super(IPPOOLS,self).__init__(ip)
        self.ip=ip
    def process_request(self,request,spider):
        # ips=requests
        thisip=random.choice(ips)
        print("当前使用的ip是：",thisip)
        # print("当前使用的ip是：",'14.29.84.50:8080')
        request.meta['proxy']='http://'+thisip.strip()
        # request.meta['proxy']='http://'+'14.29.84.50:8080'

# from Test.settings import USERAGENTPOOL
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
# from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
from fake_useragent import UserAgent
ua=UserAgent()
class UserAgent(UserAgentMiddleware):
    def __init__(self,ua=''):
        super(UserAgent,self).__init__(ua)
        self.ua=ua
    def process_request(self, request, spider):
        # thisua=random.choice(USERAGENTPOOL)
        thisua=ua.random
        print("当前使用的用户代理是：",thisua)
        request.headers.setdefault('User-Agent',thisua)