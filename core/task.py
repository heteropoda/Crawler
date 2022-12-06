
import copy
from apscheduler.schedulers.blocking import BlockingScheduler

from core.start import start
from tool.dir import check_dir_create


class Task(dict):
    
    def __init__(self) -> None:
        pass
    
    def __init__(self, dic: dict) -> None:
        self.update(dic)
    
    def run(self, settings={}):
        settings['TASK_SETTINGS'] = self
        # 输出设置
        if self.get('out_type') == 'local':
            settings['ITEM_PIPELINES'] = {'crawler.pipelines.local.LocalPipeline': 300}
        elif self.get('out_type') == 'hdfs':
            settings['ITEM_PIPELINES'] = {'crawler.pipelines.hdfs.HDFSPipeline': 300}
        # 日志设置
        settings['LOG_FILE'] = f'log/{self["name"]}.txt'
        check_dir_create('log')
        
        start(self['spider'], settings)
        
    def run_scheduler(self, settings={}):
        sched = BlockingScheduler()
        sched.add_job(self.run, 'cron', day='*', values=(settings,))
        sched.start()
    
    