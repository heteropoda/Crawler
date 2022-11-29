import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

os.environ['SCRAPY_SETTINGS_MODULE'] = 'crawler.settings'


def start(name, settings={}, *args, **kwargs):
    scrapy_settings = get_project_settings()
    scrapy_settings.update(settings)
    process = CrawlerProcess(scrapy_settings)
    process.crawl(name, *args, **kwargs)
    process.start()
    
    
if __name__ == "__main__":
    start('twitter_advanced')