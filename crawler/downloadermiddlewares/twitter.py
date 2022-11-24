# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import time
from scrapy import Request, signals

from common import TWITTER_TOKEN_URL


class TwitterDownloaderMiddleware:
    
    twitter_token = ''
    token_time = 0

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        #
        if int(time.time()) - self.token_time > 60:
            self.token_time = int(time.time())
            return Request(TWITTER_TOKEN_URL, method='POST', callback=spider.parse_token, meta={'next_request': request})
        #
        self.set_twitter_token(request, spider.twitter_token)
        
        return None

    def process_response(self, request, response, spider):
        return response

    def set_twitter_token(self, request, token):
        request.headers.update({'x-guest-token': token})

    def spider_opened(self, spider):
        spider.logger.info('TwitterDownloaderMiddleware running...')
