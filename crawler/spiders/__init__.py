# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import json
import time
import scrapy
from scrapy.http.request import Request

from common import TOKEN_URL


class BaseSpider(scrapy.Spider):
    pass


class TwitterBaseSpider(BaseSpider):
    
    token = ''
    token_time = 0
    
    def get_token(self, ignore_time=False):
        if not ignore_time and int(time.time()) - self.token_time < 60:
            return
        self.token_time = int(time.time())
        return Request(TOKEN_URL, method='POST', callback=self.parse_token)
        
    def parse_token(self, response):
        self.token = json.loads(response.text)['guest_token']