# encoding: utf-8

import copy
import json
from urllib import parse
from scrapy.http.request import Request

from common.twitter import *
from crawler.spiders import TwitterBaseSpider


class TwitterAdvancedSpider(TwitterBaseSpider):
    name = 'twitter_advanced'

    def start_requests(self):
        if 'q' not in self.settings['TASK_SETTINGS']:
            self.log('ERROR', 'NONE', 'task中无q参数')
            return 
        q = parse.quote(self.settings['TASK_SETTINGS']['q'])
        yield Request(TWITTER_ADVANCED_URL.format(q,''), meta={'q': q, 'page': 1})


    def parse(self, response):
        tweets = response.json().get('globalObjects',{}).get('tweets')
        if not tweets:
            self.log('WARN', 'MISS', f'advanced查询没有tweet Q:<{response.meta["q"]}>')
            return 
        
        for i in tweets.values():
            variables_ = copy.deepcopy(TWEET_PARAM)
            variables_['focalTweetId'] = i['id_str']
            yield Request(TWEET_URL.format(parse.quote(json.dumps(variables_).replace(' ',''))), 
                          meta={'id': i['id_str'], 'page': 0}, callback=self.parse_tweet)
            
        if self.settings['TASK_SETTINGS'].get('page_limit') and response.meta['page'] >= self.settings['TASK_SETTINGS']['page_limit']: return
        response.meta['page'] += 1
        next = response.json().get('timeline',{}).get('instructions')
        if not next: return
        if len(next) > 1:
            if next[-1].get('replaceEntry',{}).get('entry',{}).get('content',{}).get('operation',{}).get('cursor',{}).get('value'): return
            cursor = parse.quote(next[-1]['replaceEntry']['entry']['content']['operation']['cursor']['value'])
            yield Request(TWITTER_ADVANCED_URL.format(response.meta['q'], cursor), meta=response.meta)
        else:
            if next[0].get('addEntries',{}).get('entries',[{}])[-1].get('content',{}).get('operation',{}).get('cursor',{}).get('value'): return
            cursor = parse.quote(next[0]['addEntries']['entries'][-1]['content']['operation']['cursor']['value'])
            yield Request(TWITTER_ADVANCED_URL.format(response.meta['q'], cursor), meta=response.meta)
            
    def parse_tweet(self, response):
        replies = response.json().get('data',{}).get('threaded_conversation_with_injections',{}).get('instructions',[{}])[0].get('entries')
        if not replies:
            self.log('WARN', 'MISS', f'tweet没有内容 id:<{response.meta["id"]}>')
            return 
        yield {'name': response.meta['id'] + '_' + str(response.meta['page']), 'file': response.text}
        self.log('INFO', 'SUCCESS', f'抓取到原数据 id:<{response.meta["id"]}>')
        
        if replies[-1].get('entryId','').startswith('cursor'):
            variables_ = copy.deepcopy(TWEET_PARAM)
            variables_['focalTweetId'] = response.meta['id']
            variables_['cursor'] = replies[-1]['content']['itemContent']['value']
            response.meta['page'] += 1
            yield Request(TWEET_URL.format(parse.quote(json.dumps(variables_).replace(' ',''))), meta=response.meta, callback=self.parse_tweet)

        