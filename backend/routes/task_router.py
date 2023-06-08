from fastapi import APIRouter, Path, Body
from typing import List
from data.tasks import tasks
from schemas.Task import Task
from data.tasks import tasks
from services.task_services import TaskService
from config.database import Session
from fastapi.encoders import jsonable_encoder

task_router = APIRouter()

db = Session()


@task_router.get('/api/tasks', tags=['Task'])
def get_tasks():
    response = TaskService(db).get_tasks()
    return {'info': 'Success', 'data': jsonable_encoder(response)}

@task_router.get('/api/task/{task_id}', tags=['Task'])
def get_task(task_id: int = Path(ge=1, le=1000)):
    response = TaskService(db).get_task(task_id)
    return response


@task_router.get('/api/task/done/{task_id}', tags=['Task'])
def get_done_task(task_id: int):
    response = TaskService(db).get_done_task(task_id)
    return response


@task_router.get('/api/task/undone/{task_id}', tags=['Task'])
def get_undone_task(task_id: int = Path(ge=1, le=1000)):
    response = TaskService(db).get_undone_task(task_id)
    return response


@task_router.post('/api/task', tags=['Task'])
def create_task(task: Task = Body()):
    response = TaskService(db).create_task(task)
    return response


@task_router.put('/api/task/{task_id}', tags=['Task'])
def update_task(task_id: int, task: Task = Body()):
    response = TaskService(db).update_task(task_id, task)
    return response


@task_router.delete('/api/task/{task_id}', tags=['Task'])
def delete_task(task_id: int):
    response = TaskService(db).delete_task(task_id)
    return response
