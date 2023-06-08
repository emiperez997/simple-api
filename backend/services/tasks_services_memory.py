from data.tasks import tasks
from schemas.Task import Task


class TaskService():
    def __init__(self):
        self.tasks = tasks

    def get_tasks(self):
        return self.tasks

    def get_task(self, task_id: int):
        task = next((task for task in self.tasks if task['id'] == task_id), {})
        return {'info': 'Success', 'data': task} if task else {'error': 'Task not found'}

    def get_done_task(self, task_id: int):
        task = next((task for task in self.tasks if task['id'] == task_id), {})
        if task:   
          if task['done']:
            return {'message': 'Task already done'}
          else:
            task['done'] = True
            return {'message': 'Task done', 'task': task}

        return {'error': 'Task not found'}

    def get_undone_task(self, task_id: int):
        task = next((task for task in self.tasks if task['id'] == task_id), {})
        if task:   
          if not task['done']:
            return {'message': 'Task already undone'}
          else:
            task['done'] = False
            return {'message': 'Task undone', 'task': task}

        return {'error': 'Task not found'}

    def create_task(self, task: Task):
        self.tasks.append({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'done': task.done
        })
        return {'info': 'Task created', 'data': self.tasks}

    def update_task(self, task_id: int, task: Task):
        task_found = next((t for t in tasks if t['id'] == task_id), None)
        if task_found:
            task_found["title"] = task.title
            task_found["description"] = task.description
            task_found["done"] = task.done

            return {'info': 'Task updated', 'data': task_found}
        else:
            return {'error': 'Task not found'}
    
    def delete_task(self, task_id: int):
        task_found = next((t for t in tasks if t['id'] == task_id), None)
        if task_found:
            tasks.remove(task_found)
            return {'info': 'Task deleted', 'data': tasks}
        else:
            return {'error': 'Task not found'}
