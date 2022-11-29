
from core.start import start


class Task:
    
    def __init__(self) -> None:
        pass
    
    def __init__(self, name, spider) -> None:
        self.name = name
        self.spider = spider
    
    def run(self, settings={}):
        dic = self.__dict__
        settings['TASK_SETTINGS'] = dic
        # 输出类型
        if dic.get('out_type') == 'hbase':
            pass
        #
        start(self.spider, settings)
    
    
    
class TwitterAdvancedTask(Task):
    pass
    
    
if __name__ == "__main__":
    task = TwitterAdvancedTask('demo_task', 'twitter_advanced')
    task.q = "(from:elonmusk) since:2022-11-27"
    task.run()
    