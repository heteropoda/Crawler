
from common.task import DEFAULT_TASK
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
        'q': '(from:elonmusk) since:2022-11-27'
    })
    task.run()