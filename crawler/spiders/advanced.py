# # encoding: utf-8

# import json
# import copy
# import re
# from urllib import parse

# from crawler.items import TweetItem
# from crawler.spiders import BaseSpider
# from utils.date_util import DateUtil
# from utils.format_util import FormatUtil
# from common.request import *
# from scrapy.http.request import Request

# class AdvancedSpider(BaseSpider):
#     name = 'advanced'
#     custom_settings = {"DEFAULT_REQUEST_HEADERS": TWITTER_DEFAULT_HEADER}
#     config = 'advanced_config.json'
#     proxy = '01'

#     def start_requests(self, **kwargs):
#         try:
#             for i in kwargs.keys():
#                 setattr(self, i, kwargs[i])
#             js = json.load(open('config/' + self.config, 'r', encoding='utf-8'))
#             for config_list in js:
#                 q_list = FormatUtil.q_format(config_list)
#                 for q_ in q_list:
#                     yield Request(ADVANCED_URL.format(parse.quote(q_),''), meta={'q': q_})
#         except Exception as e:
#             self.send_log(3, "start_requests出错 ==> {}".format(e))


#     def parse(self, response):
#         tweets = response.json().get('globalObjects',{}).get('tweets')
#         if not tweets:
#             return 
#         self.send_log(1, "高级搜索成功 ==> q:<{}>".format(response.meta['q']))
#         user_name = response.json()['globalObjects']['users'].values()
#         user_name = list(user_name)[0]['screen_name']

#         for i in tweets.values():
#             try:
#                 item = TweetItem()
#                 item['id'] = i['id']
#                 item['q'] = response.meta['q']
#                 item['content'] = i['full_text']
#                 content_del = re.findall(r'https://t.co/\S+?$', item['content'])
#                 item['content'] = item['content'].replace(content_del[0],'') if content_del else item['content']
#                 item['uname'] = user_name
#                 item['pub_time'] = DateUtil.format_time_twitter(i['created_at'])
#                 item['url'] = 'https://twitter.com/{}/status/{}'.format(item['uname'],item['id'])
#                 item['retweet_count'] = i['retweet_count']
#                 item['favorite_count'] = i['favorite_count']
#                 item['reply_count'] = i['reply_count']
#                 item['quote_count'] = i['quote_count']
#                 item['replies'] = []
#                 item['entities'] = []
#                 for j in i.get('entities',{}).get('media',[]):
#                     item['entities'].append(j['media_url_https'])

#                 variables_ = copy.deepcopy(TWEET_PARAM)
#                 variables_['focalTweetId'] = i['id_str']
#                 yield Request(TWEET_URL.format(parse.quote(json.dumps(variables_).replace(' ',''))), meta={'item': item}, callback=self.parse_item)
#             except Exception as e:
#                 self.send_log(3, "item解析出错 ==> {} ==> url:<{}>".format(e, response.url))

#         next = response.json().get('timeline',{}).get('instructions')
#         if next:
#             if len(next) > 1:
#                 if next[-1].get('replaceEntry',{}).get('entry',{}).get('content',{}).get('operation',{}).get('cursor',{}).get('value'):
#                     cursor = parse.quote(next[-1]['replaceEntry']['entry']['content']['operation']['cursor']['value'])
#                     yield Request(ADVANCED_URL.format(parse.quote(response.meta['q']),cursor), meta=response.meta)
#             else:
#                 if next[0].get('addEntries',{}).get('entries',[{}])[-1].get('content',{}).get('operation',{}).get('cursor',{}).get('value'):
#                     cursor = parse.quote(next[0]['addEntries']['entries'][-1]['content']['operation']['cursor']['value'])
#                     yield Request(ADVANCED_URL.format(parse.quote(response.meta['q']),cursor), meta=response.meta)


#     def parse_item(self, response):
#         item_ = response.meta['item']
#         replies = response.json().get('data',{}).get('threaded_conversation_with_injections',{}).get('instructions',[{}])[0].get('entries')
#         if not replies:
#             return 
#         for items in replies:
#             for i in items.get('content',{}).get('items',[]):
#                 i = i.get('item',{}).get('itemContent',{}).get('tweet_results',{}).get('result',{})
#                 if not i:
#                     continue
#                 user_name = i['core']['user_results']['result']['legacy']['screen_name']
#                 i = i['legacy']

#                 try:
#                     item = TweetItem()
#                     item['id'] = int(i['id_str'])
#                     item['content'] = i['full_text']
#                     content_del = re.findall(r'https://t.co/\S+?$', item['content'])
#                     item['content'] = item['content'].replace(content_del[0],'') if content_del else item['content']
#                     item['uname'] = user_name
#                     item['pub_time'] = DateUtil.format_time_twitter(i['created_at'])
#                     item['url'] = 'https://twitter.com/{}/status/{}'.format(item['uname'],item['id'])
#                     item['retweet_count'] = i['retweet_count']
#                     item['favorite_count'] = i['favorite_count']
#                     item['reply_count'] = i['reply_count']
#                     item['quote_count'] = i['quote_count']
#                     item['entities'] = []
#                     for j in i.get('entities',{}).get('media',[]):
#                         item['entities'].append(j['media_url_https'])

#                     item_['replies'].append(dict(item))
#                 except Exception as e:
#                     self.send_log(3, "reply解析出错 ==> {} ==> url:<{}>".format(e, response.url))

#         if replies[-1].get('entryId','').startswith('cursor'):
#             variables_ = copy.deepcopy(TWEET_PARAM)
#             variables_['focalTweetId'] = str(item_['id'])
#             variables_['cursor'] = replies[-1]['content']['itemContent']['value']
#             yield Request(TWEET_URL.format(parse.quote(json.dumps(variables_).replace(' ',''))), meta={'item': item_}, callback=self.parse_item)
#         else:
#             yield item_
#             self.send_log(1, "tweet获取成功 ==> tweet_id:<{}>".format(str(item_['id'])))