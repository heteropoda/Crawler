
import time
from itemadapter import ItemAdapter

from tool.dir import check_dir_create


class LocalPipeline:
    
    def process_item(self, item, spider):
        with open(f'{self.out_path}/{item["name"]}','w', encoding='utf-8') as f:
            f.write(item['file'])
        return item
    
    def open_spider(self, spider):
        task_name = spider.settings['TASK_SETTINGS'].get('name', 'default')
        self.out_path = spider.settings['TASK_SETTINGS'].get('out_path','out')
        self.out_path += f'/{task_name}/{int(time.time())}'
        check_dir_create(self.out_path)
        