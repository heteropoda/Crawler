# encoding: utf-8
'''
Description: get_advanced生成脚本
Version: 1.0
Autor: Renhetian
Date: 2022-01-03 20:35:40
LastEditors: Renhetian
LastEditTime: 2022-02-22 17:55:23
'''

import json
import copy
import fire

default_config = {
    "words": [],
    "none_words": [],
    "hashtags": [],
    "language": "",
    "from": [],
    "to": [],
    "mention": [],
    "filter_links": None,
    "filter_replies": None,
    "min_reply": 0,
    "min_like": 0,
    "min_retweet": 0,
    "until": "",
    "since": "",
    "step": ""
}

# 搜索词
# word_list = [["COVID-19","COVID","COVID19","Covid19"],"Delta variant","pandemic","epidemic","vaccine","Virus","Coronavirus","biolab","medical supplies","outbreak","Wuhan"]
word_list = ["OBOR", "Belt and Road", "B&R", "Silk Road", "One Belt One Road"]
# 发布者
# from_ = ["ChineseEmbinUK"]
# from_ = ["ChinaDaily"]
from_ = []
# 截止时间
until = ""
# 开始时间
since = "2020-10-01"
# 步长
step = "month"

def run(file_name):
    ll = []
    with open('config/' + file_name, 'w', encoding='utf-8') as file:
        for i in word_list:
            config = copy.deepcopy(default_config)
            config['until'] = until
            config['since'] = since
            config['step'] = step
            config['from'] = from_
            config['words'] = [i]
            ll.append(config)
        file.write(json.dumps(ll,ensure_ascii=False))


# 拉取advanced配置脚本
# python -m scripts.get_advanced --file_name=advanced_config.json
if __name__ == "__main__":
    fire.Fire(run)