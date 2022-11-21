# encoding: utf-8

import json
from urllib import parse
import requests
from scrapy.http.request import Request

from common import *
from crawler.spiders import TwitterBaseSpider


class TwitterAdvancedSpider(TwitterBaseSpider):
    name = 'twitter_advanced'
    custom_settings = {"DEFAULT_REQUEST_HEADERS": TWITTER_DEFAULT_HEADER}

    def start_requests(self, **kwargs):
        q = "%22Belt%20and%20Road%22%20%28from%3Achinadaily%29%20until%3A2020-09-05%20since%3A2020-08-06"
        yield Request(ADVANCED_URL.format(parse.quote(q),''), meta={'q': q})


    def parse(self, response):
        tweets = response.json().get('globalObjects',{}).get('tweets')
        if not tweets:
            return 
        
    def get_token(self):
        res = requests.post(TOKEN_URL)
        self.token = json.loads(res.text)['guest_token']
        