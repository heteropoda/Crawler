
from common.twitter import TWITTER_DEFAULT_HEADER
from tool.dir import check_dir_create


def get_custom_settings(name):
    s = {}
    
    if name.startswith('twitter'):
        s.update(get_twitter_custom_settings(name))
    
    return s
    
def get_twitter_custom_settings(name):
    s = {
        "DEFAULT_REQUEST_HEADERS": TWITTER_DEFAULT_HEADER,
        "DOWNLOADER_MIDDLEWARES": {
            'crawler.downloadermiddlewares.twitter.TwitterDownloaderMiddleware': 543,
        },
        "LOG_FILE": 'log/twitter.txt'
    }
    
    if name.startswith('twitter_advanced'):
        s.update({"LOG_FILE": 'log/twitter_advanced.txt'})
        
    return s
    