from fastapi import APIRouter, Path, Body
from typing import List
from data.tasks import tasks
from schemas.Task import Task
from services.tasks_services_memory import TaskService
from data.tasks import tasks

task_router = APIRouter()


@task_router.get('/api/tasks', tags=['Task'], response_model=List[Task])
def get_tasks() -> List[Task]:
    return tasks


@task_router.get('/api/task/{task_id}', tags=['Task'])
def get_task(task_id: int = Path(ge=1, le=1000)) -> dict:
    response = TaskService().get_task(task_id)
    return response


@task_router.get('/api/task/done/{task_id}', tags=['Task'])
def get_done_task(task_id: int) -> dict:
    response = TaskService().get_done_task(task_id)
    return response


@task_router.get('/api/task/undone/{task_id}', tags=['Task'])
def get_undone_task(task_id: int = Path(ge=1, le=1000)) -> dict:
    response = TaskService().get_undone_task(task_id)
    return response


@task_router.post('/api/task', tags=['Task'])
def create_task(task: Task = Body()) -> dict:
    response = TaskService().create_task(task)
    return response


@task_router.put('/api/task/{task_id}', tags=['Task'])
def update_task(task_id: int, task: Task = Body()) -> dict:
    response = TaskService().update_task(task_id, task)
    return response


@task_router.delete('/api/task/{task_id}', tags=['Task'])
def delete_task(task_id: int) -> dict:
    response = TaskService().delete_task(task_id)
    return response
