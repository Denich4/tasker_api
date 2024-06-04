from flask import request
from models.models import Task
from db import db, connection, metadata, engine, Base
from sqlalchemy.orm import Session

from utils.strDateUtil import strToDate

session = Session(autoflush=False, bind=engine)

def get_tasks():
    tasks = session.query(Task).all()
    return tasks

def post_task(task_name, task_is_termless, task_date, task_description=''):
    default_status_id_done = False
    new_task = Task(
        task_name=task_name, 
        task_is_done=default_status_id_done, 
        task_is_termless=task_is_termless, 
        task_date=task_date,
        task_description=task_description
        )
    session.add(new_task)
    session.commit()
    return new_task