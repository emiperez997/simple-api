from fastapi import APIRouter, Path, Body
from typing import List
from schemas.Task import Task
from controllers.task_controller import TaskController

task_router = APIRouter()

@task_router.get('/api/tasks', tags=['Task'])
def get_tasks():
    response = TaskController().get_tasks()
    return response

@task_router.get('/api/task/{task_id}', tags=['Task'])
def get_task(task_id: int = Path(ge=1, le=1000)):
    response = TaskController().get_task(task_id)
    return response


@task_router.get('/api/task/done/{task_id}', tags=['Task'])
def get_done_task(task_id: int):
    response = TaskController().get_done_task(task_id)
    return response


@task_router.get('/api/task/undone/{task_id}', tags=['Task'])
def get_undone_task(task_id: int = Path(ge=1, le=1000)):
    response = TaskController().get_undone_task(task_id)
    return response

@task_router.get('/api/tasks/done', tags=['Task'])
def get_all_done():
    response = TaskController().get_all_done()
    return response


@task_router.post('/api/task', tags=['Task'])
def create_task(task: Task = Body()):
    response = TaskController().create_task(task)
    return response


@task_router.put('/api/task/{task_id}', tags=['Task'])
def update_task(task_id: int, task: Task = Body()):
    response = TaskController().update_task(task_id, task)
    return response


@task_router.delete('/api/task/{task_id}', tags=['Task'])
def delete_task(task_id: int):
    response = TaskController().delete_task(task_id)
    return response
