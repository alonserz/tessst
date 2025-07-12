import os
from fastapi import FastAPI, status, Request
from fastapi.responses import JSONResponse
from backend.find import (
    find_substring,
    get_task_by_id,
)
from db import (
    add_new_task_to_db,
    get_all_tasks_db,
    get_data_by_task_id_db,
    set_task_ready_db
)
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine

templates = Jinja2Templates(directory='frontend')
app = FastAPI()

postgress_dbname = os.getenv('POSTGRESQL_DB_NAME', default='postgres') 
postgress_username = os.getenv('POSTGRESQL_USER_NAME')
postgress_pass = os.getenv('POSTGRESQL_PASSWORD')
postgress_host = os.getenv('POSTGRESQL_HOST', 'postgresql')

engine = create_engine(f'postgresql://{postgress_username}:{postgress_pass}@postgres:5432/{postgress_dbname}')

@app.get("/find_substring/{substring}")
def find_substring_route(substring: str):
    substring = str(substring)
    task = find_substring.delay('./backend/data/data.csv', substring)
    task_id = task.id
    is_ready = task.ready()
    add_new_task_to_db(engine, task_id, substring, is_ready)
    return JSONResponse(status_code = status.HTTP_200_OK, content = (task_id, is_ready, substring))

@app.get('/')
def main(request: Request):
    tasks = get_all_tasks_db(engine)
    data = []
    for task in tasks:
        set_task_ready_db(engine, task[0])
        data.append((task[0], task[1], task[2]))
    return templates.TemplateResponse("index.html", {'request': request, 'data': tuple(data)})

@app.get('/get_data_by_task_id/{task_id}')
def get_data_route(task_id):
    task = get_data_by_task_id_db(engine, task_id)
    data = []
    if task:
        task_id = task[0]
        task = get_task_by_id(task_id)
        if task.ready():
            data = tuple(task.collect())[0][1]
    return JSONResponse(status_code = status.HTTP_200_OK, content = data)
