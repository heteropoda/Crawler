
from core.task import Task


if __name__ == "__main__":
    task = Task({
        'name': 'task1',
        'spider': 'twitter_advanced',
        'run_type': '',
        'corn': '',
        'out_type': 'local',
        'out_path': 'out',
        'page_limit': 0,
        # 'hdfs_host': 'http://192.168.202.128:9870',
        'q': '(from:elonmusk) until:2022-12-02 since:2022-12-01',
    })
    task.run()