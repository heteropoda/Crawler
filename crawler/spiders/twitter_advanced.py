# encoding: utf-8

import copy
import json
from urllib import parse
from scrapy.http.request import Request

from common import *
from crawler.spiders import TwitterBaseSpider


class TwitterAdvancedSpider(TwitterBaseSpider):
    name = 'twitter_advanced'
    

    def start_requests(self, **kwargs):
        q = "%22Belt%20and%20Road%22%20%28from%3Achinadaily%29%20until%3A2020-09-05%20since%3A2020-08-06"
        yield Request(TWITTER_ADVANCED_URL.format(parse.quote(q),''), meta={'q': q})


    def parse(self, response):
        tweets = response.json().get('globalObjects',{}).get('tweets')
        if not tweets:
            return 
        
        for i in tweets.values():
            variables_ = copy.deepcopy(TWEET_PARAM)
            variables_['focalTweetId'] = i['id_str']
            yield Request(TWEET_URL.format(parse.quote(json.dumps(variables_).replace(' ',''))), meta={}, callback=self.parse_tweet)
            
    def parse_tweet(self, response):
        pass

        