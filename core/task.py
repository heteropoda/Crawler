
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
        # 日志设置
        settings['LOG_FILE'] = f'log/{self.name}.txt'
        check_dir_create(settings['LOG_FILE'])
        
        start(self['spider'], settings)
        
    def run_scheduler(self, settings={}):
        sched = BlockingScheduler()
        sched.add_job(self.run, 'cron', day='*', values=(settings,))
        sched.start()
    
    
    
if __name__ == "__main__":
    task = Task({'name':'demo_task', 'spider':'twitter_advanced'})
    task['q'] = "(from:elonmusk) since:2022-11-27"
    task['out_type'] = 'local'
    task['out_path'] = 'out'
    task.run()
    