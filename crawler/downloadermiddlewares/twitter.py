# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import time
from scrapy import Request, signals

from common.twitter import TWITTER_TOKEN_URL


class TwitterDownloaderMiddleware:
    
    token_time = 0

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # 获取token
        if int(time.time()) - self.token_time > 60:
            self.token_time = int(time.time())
            request.dont_filter = True
            return Request(TWITTER_TOKEN_URL, method='POST', dont_filter=True,
                           callback=spider.parse_token, meta={'next_request': request})
        # 加入token
        request.headers.update({'x-guest-token': spider.twitter_token})
        
        return None

    def process_response(self, request, response, spider):
        return response

    def spider_opened(self, spider):
        spider.logger.info('TwitterDownloaderMiddleware running...')
