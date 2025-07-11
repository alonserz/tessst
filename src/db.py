from sqlalchemy import text


def add_new_task_to_db(engine, task_id, substring, is_ready):
    with engine.connect() as connection:
        connection.execute(text("CREATE TABLE IF NOT EXISTS tasks (id varchar, substring varchar, is_ready boolean)"))
        connection.execute(text(f"INSERT INTO tasks VALUES ('{task_id}', '{substring}', {is_ready})"))
        connection.commit()

def get_all_tasks_db(engine):
    with engine.connect() as connection:
        connection.execute(text("CREATE TABLE IF NOT EXISTS tasks (id varchar, substring varchar, is_ready boolean)"))
        data = connection.execute(text("select * from tasks"))
        connection.commit()
    return data

def get_data_by_task_id_db(engine, task_id):
    with engine.connect() as connection:
        connection.execute(text("CREATE TABLE IF NOT EXISTS tasks (id varchar, substring varchar, is_ready boolean)"))
        data = connection.execute(text(f"select * from tasks where id = '{task_id}'"))
        data = data.fetchone()
        connection.commit()
    return data

def set_task_ready_db(engine, task_id):
    with engine.connect() as connection:
        connection.execute(text("CREATE TABLE IF NOT EXISTS tasks (id varchar, substring varchar, is_ready boolean)"))
        connection.execute(text(f"update tasks set is_ready=true where id='{task_id}'"))
        connection.commit()
