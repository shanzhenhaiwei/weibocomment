# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from fake_useragent import UserAgent

class WeibocommentSpiderMiddleware(object):
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


class WeibocommentDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class RandomUserAgentMiddleware():
    def __init__(self):
        self.ua = UserAgent()

    def process_request(self,request,spider):
        request.headers['User-Agent']=self.ua.random
        request.cookies={'SINAGLOBAL': '9080164014087.543.1539352419143', 'UOR': 'www.google.com.hk,www.weibo.com,www.google.com.hk', 'YF-Page-G0': 'aabeaa17d9557111c805fb15a9959531', '_s_tentry': '-', 'Apache': '7081746279126.242.1542010072747', 'ULV': '1542010072786:16:6:1:7081746279126.242.1542010072747:1541773720789', 'YF-Ugrow-G0': '8751d9166f7676afdce9885c6d31cd61', 'YF-V5-G0': 'f0aa2e6d566ccd1c288fae19df01df56', 'WBtopGlobal_register_version': '520db7b0c48d3596', 'SSOLoginState': '1542010117', 'wb_view_log_5694346595': '1366*7681', 'SCF': 'As7wKYQH6AhUz7PGG4nvsAB2jWeUpC_K67uvQmV_q1nAIyhUdmmew3BSFSHw_TbBAMaN1Z_CS3MCfETjn3L2mlo.', 'SUB': '_2A2527vjgDeRhGeNI4lYS9CjJwjmIHXVVmm0orDV8PUJbmtAKLWGnkW9NSAIjQREnJ3dhcAwErpnzcDAVvdcjMqXi', 'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WWUhrLSOmm3bM-0pZMKiyEK5JpX5K-hUgL.Fo-c1KB0Shqf1K-2dJLoIpXLxK-LBo5L12qLxK-LBKBLBoBLxK.L1KzL1hyRd5tt', 'SUHB': '010GyHBo7bEbTx', 'ALF': '1573632736'}


    def process_response(self,request,response,spider):
        if response.status != 200:
            print('状态码错误',response.status)
            print('error url=',request.url)
            f=open('/home/jiemaohua/Desktop/spiderprojects/weibocomment/logs/log.txt','a')
            f.write(request.url)
            f.close()
            return request
        return response






