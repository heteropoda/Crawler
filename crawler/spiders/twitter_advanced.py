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
        q = "(from:elonmusk)"
        yield Request(TWITTER_ADVANCED_URL.format(parse.quote(q),''), meta={'q': q})


    def parse(self, response):
        tweets = response.json().get('globalObjects',{}).get('tweets')
        if not tweets:
            self.logger.warning(f'没有tweet url:<{response.url}>')
            return 
        
        for i in tweets.values():
            variables_ = copy.deepcopy(TWEET_PARAM)
            variables_['focalTweetId'] = i['id_str']
            yield Request(TWEET_URL.format(parse.quote(json.dumps(variables_).replace(' ',''))), meta={}, callback=self.parse_tweet)
            
        next = response.json().get('timeline',{}).get('instructions')
        if next:
            if len(next) > 1:
                if next[-1].get('replaceEntry',{}).get('entry',{}).get('content',{}).get('operation',{}).get('cursor',{}).get('value'):
                    cursor = parse.quote(next[-1]['replaceEntry']['entry']['content']['operation']['cursor']['value'])
                    yield Request(TWITTER_ADVANCED_URL.format(parse.quote(response.meta['q']),cursor), meta=response.meta)
            else:
                if next[0].get('addEntries',{}).get('entries',[{}])[-1].get('content',{}).get('operation',{}).get('cursor',{}).get('value'):
                    cursor = parse.quote(next[0]['addEntries']['entries'][-1]['content']['operation']['cursor']['value'])
                    yield Request(TWITTER_ADVANCED_URL.format(parse.quote(response.meta['q']),cursor), meta=response.meta)
            
    def parse_tweet(self, response):
        replies = response.json().get('data',{}).get('threaded_conversation_with_injections_v2',{}).get('instructions',[{}])[0].get('entries')
        if not replies:
            return 
        yield {'text': response.text}
        
        if replies[-1].get('entryId','').startswith('cursor'):
            variables_ = copy.deepcopy(TWEET_PARAM)
            variables_['cursor'] = replies[-1]['content']['itemContent']['value']
            yield Request(TWEET_URL.format(parse.quote(json.dumps(variables_).replace(' ',''))), meta=response.meta, callback=self.parse_item)

        