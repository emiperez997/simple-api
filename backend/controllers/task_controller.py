from models.task_model import Task as TaskModel
from services.task_services import TaskService
from config.database import Session
from fastapi.encoders import jsonable_encoder

class TaskController():
    def __init__(self) -> None:
        self.db = Session()

    def get_tasks(self):
        result = TaskService(self.db).get_tasks()
        return result

    def get_done_task(self, id: int):
        try:
            task = TaskService(self.db).get_done_task(id)
            if task:
                return {'info': 'Task done', 'task': TaskService(self.db).get_task(id) }
            
            elif task == None:
                return {'error': 'Task not found'}
            
            else:
                return {'error': 'Task already done'}
        except:
            return {'error': 'Error doing task', 'message': f"{error}", 'status': 500}

    def get_undone_task(self, id: int):
        try:
            task = TaskService(self.db).get_undone_task(id)
            if task:
                return {'info': 'Task undone', 'task': TaskService(self.db).get_task(id) }
            
            elif task == None:
                return {'error': 'Task not found'}
            
            else:
                return {'error': 'Task already undone'}
        except:
            return {'error': 'Error doing task', 'message': f"{error}", 'status': 500}
      
    def get_all_done(self):
        # tasks_undone = self.db.query(TaskModel).filter(TaskModel.done == False).all()

        # print(tasks_undone)

        # if tasks_undone:
        #     for task in tasks_undone:
        #         task.done = True
        #     self.db.commit()
        #     return {'info': 'All tasks done', 'tasks': self._get_all()}

        # return {'error': 'All tasks already done'}
        try:
            tasks_done = TaskService(self.db).get_all_done()

            if tasks_done:
                return {'info': 'All tasks done', 'tasks': tasks_done}

            else:
                return {'error': 'All tasks already done'}

        except Exception as error:
            return {'error': 'Error doing task', 'message': f"{error}", 'status': 500}



    def get_task(self, id):
        task = TaskService(self.db).get_task(id)
        if task:
            return {'info': 'Success', 'data': task}
        else:
            return {'error': 'Task not found'}


    def create_task(self, task):
        try:
            new_task = TaskModel(**task.dict())
            TaskService(self.db).create_task(new_task)
            tasks = TaskService(self.db).get_tasks() 
            return {'info': 'Task created', 'data': jsonable_encoder(tasks)}
        except Exception as error: 
            print(error)
            return {'error': 'Error creating task', 'message': error, 'status': 500}
        

    def update_task(self, id, task):
        try:
            task = TaskService(self.db).update_task(id, task)
            if task:
                return {'info': 'Task updated', 'data': task }
            
            else:
                return {'error': 'Task not found'}

        except Exception as error:
            return {'error': 'Error updating task', 'message': f"{error}", 'status': 500}


    def delete_task(self, id):
        try:
            tasks = TaskService(self.db).delete_task(id)
            if task:
                return {'info': 'Task Deleted', 'data': tasks }
            
            else:
                return {'error': 'Task not found'}

        except Exception as error:
            return {'error': 'Error updating task', 'message': f"{error}", 'status': 500}