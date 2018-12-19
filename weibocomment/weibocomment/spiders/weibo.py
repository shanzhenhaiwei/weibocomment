# -*- coding: utf-8 -*-
import re
import scrapy
import json
from pyquery import PyQuery as pq
# from scrapy import Spider,Request
# from urllib.parse import urlencode
import time
from weibocomment.items import WeibocommentItem


current_milli_time = lambda: int(round(time.time() * 1000))

class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['weibo.com']
    start_urls=['https://weibo.com/aj/v6/comment/big?ajwvr=6&id=4278485968873068&page=4979']
    url_count=4979

    def parse(self, response):
        if response:
            dic = json.loads(response.body)
            html = dic['data']['html']
            doc = pq(html)
            items = doc('.list_con').items()

            for item in items:
                if item.text():
                    data = {}
                    data['id'] = item('.list_con>.WB_text>a').text().split(' ')[0]
                    data['text'] = item('.list_con>div.WB_text').text()
                    data['time'] = item('.list_con>.WB_func>.WB_from').text()
                    _num = item('.list_con>.WB_func>.WB_handle>.clearfix').text()
                    num = re.search('ñ(\d*)', _num,re.S)
                    if num:
                        data['likenum'] = num.group(1)
                    yield data
            self.url_count=self.url_count+1
            print('1-current page=',self.url_count)
            url='https://weibo.com/aj/v6/comment/big?ajwvr=6&id=4278485968873068&page='+str(self.url_count)
            yield scrapy.Request(url)


