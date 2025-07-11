import re
import os
import csv
from celery import Celery
from celery.result import AsyncResult
from functools import lru_cache

broker_user_name = os.getenv('RABBITMQ_USER_NAME')
broker_password = os.getenv('RABBITMQ_PASSWORD')

celery_app = Celery('celery', backend='redis://redis:6379/0', broker=f'amqp://{broker_user_name}:{broker_password}@rabbitmq:5672/myvhost')

@lru_cache
def parse_file(file_path):
    data = {}
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file, delimiter = ',')
        for row in reader:
            id = row[0]
            string = row[1]
            data[id] = string
    return data

@celery_app.task
def find_substring(file_path, substring: str):
    idxes = {}
    start, end = 0, 0
    strings = parse_file(file_path)
    for key, value in strings.items():
        if not substring in str(value):
            continue
        for match in re.finditer(substring, value):
            start = match.start()
            end = match.end()
            break

        idxes[key] = {}
        idxes[key]['string'] = value
        idxes[key]['start'] = start
        idxes[key]['end'] = end
    return idxes

def get_task_by_id(task_id, app = celery_app):
    res = AsyncResult(task_id, app = app)
    return res
