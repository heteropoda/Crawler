
import datetime
import time

from common.date import ENGLISH_MONTH


def time_now_formate():
        '''
        返回当前的格式化时间，格式：%Y-%m-%d %H:%M:%S
        '''
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


def formate_time2time_stamp(time_):
        '''
        将传入的格式化时间转为时间戳，格式：%Y-%m-%d
        '''
        return int(time.mktime(time.strptime(time_, "%Y-%m-%d")))


def time_stamp2formate_time(time_):
        '''
        将传入的时间戳转为格式化时间，格式：%Y-%m-%d
        '''
        return time.strftime("%Y-%m-%d", time.localtime(int(time_)))


def time_ago(year=0, month=0, week=0, day=0, hour=0, minute=0, second=0):
        '''
        返回指定时间之前的时间戳
        '''
        stamp = int(time.time()) - second - minute*60 - hour*3600 - day*86400 - week*604800 - month*2592000 - year*31536000
        return (stamp if stamp > 0 else 0)


def format_time_twitter(data1):
        '''
        格式化twitter时间字符串，格式：%Y-%m-%d %H:%M:%S
        Thu Sep 30 06:38:07 +0000 2021
        '''
        dl = data1.split(' ')
        out = datetime.datetime(int(dl[5]),ENGLISH_MONTH[dl[1]],int(dl[2])).strftime("%Y-%m-%d ")
        return out + dl[3]