
import time
from hdfs.client import Client


class HDFSPipeline:
    
    def process_item(self, item, spider):
        self.cli.write(f'{self.out_path}/{item["name"]}', 
                       item['file'].encode('utf-8').decode('latin-1'), overwrite=True, append=False)
        return item
    
    def open_spider(self, spider):
        hdfs_url = spider.settings['TASK_SETTINGS'].get('hdfs_host', 'http://localhost:9870')
        task_name = spider.settings['TASK_SETTINGS'].get('name', 'default')
        self.out_path = spider.settings['TASK_SETTINGS'].get('out_path','out')
        self.out_path += f'/{task_name}/{int(time.time())}'
        
        self.cli = Client(hdfs_url)
        self.cli.makedirs(self.out_path)
        