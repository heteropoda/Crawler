# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import json
import time
import scrapy
from scrapy.http.request import Request

from common.twitter import TWITTER_DEFAULT_HEADER


class BaseSpider(scrapy.Spider):
    
    def log(self, level='DEBUG', sign='NONE', message='send a message...'):
        msg = '<{}> {}'
        if level == 'INFO':
            self.logger.info(msg.format(sign, message))
        elif level == 'WARNING' or level == 'WARN':
            self.logger.warning(msg.format(sign, message))
        elif level == 'ERROR':
            self.logger.warning(msg.format(sign, message))
        else:
            self.logger.debug(msg.format(sign, message))


class TwitterBaseSpider(BaseSpider):
    
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": TWITTER_DEFAULT_HEADER,
        "DOWNLOADER_MIDDLEWARES": {
            'crawler.downloadermiddlewares.twitter.TwitterDownloaderMiddleware': 543,
        }
    }
    
    twitter_token = ''
        
    def parse_token(self, response):
        self.twitter_token = json.loads(response.text)['guest_token']
        self.log('INFO', 'MESSAGE', 'token更新成功')
        yield response.meta['next_request']