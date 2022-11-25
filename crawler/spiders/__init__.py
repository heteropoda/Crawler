# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import json
import time
import scrapy
from scrapy.http.request import Request

from common import TWITTER_DEFAULT_HEADER


class BaseSpider(scrapy.Spider):
    pass


class TwitterBaseSpider(BaseSpider):

    twitter_token = ''
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": TWITTER_DEFAULT_HEADER,
        "DOWNLOADER_MIDDLEWARES": {
            'crawler.downloadermiddlewares.twitter.TwitterDownloaderMiddleware': 543,
        }
    }
    
    def start_requests(self, **kwargs):
        pass
        
    def parse_token(self, response):
        self.twitter_token = json.loads(response.text)['guest_token']
        self.logger.info('token更新成功')
        yield response.meta['next_request']