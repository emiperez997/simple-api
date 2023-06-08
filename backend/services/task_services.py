from models.task_model import Task as TaskModel

class TaskService():
    def __init__(self, db) -> None:
        self.db = db

    def _get_all(self):
        return self.db.query(TaskModel).all()

    def _get_one(self, id):
        return self.db.query(TaskModel).filter(TaskModel.id == id).first()

    def get_tasks(self):
        result = self.db.query(TaskModel).all()
        return result

    def get_done_task(self, id: int):
        task = self.db.query(TaskModel).filter(TaskModel.id == id).first()
        if task:
            if task.done:
                return {'error': 'Task already done'}
            else:
                task.done = True
                self.db.commit()
                return {'info': 'Task done', 'task': self._get_one(id)}

        return {'error': 'Task not found'}

    def get_undone_task(self, id: int):
        task = self.db.query(TaskModel).filter(TaskModel.id == id).first()
        if task:
            if not task.done:
                return {'error': 'Task already done'}
            else:
                task.done = False
                self.db.commit()
                return {'info': 'Task done', 'task': self._get_one(id)}

        return {'error': 'Task not found'}

    def get_task(self, id):
        task = self.db.query(TaskModel).filter(TaskModel.id == id).first()
        return {'info': 'Success', 'data': task} if task else {'error': 'Task not found'}


    def create_task(self, task):
        new_task = TaskModel(**task.dict())
        self.db.add(new_task)
        self.db.commit()
        return {'info': 'Task created', 'data': self._get_all()}

    def update_task(self, id, task):
        taskDB = self._get_one(id)
        if task:
            taskDB.title = task.title
            taskDB.description = task.description
            taskDB.done = task.done
            self.db.commit()
            return {'info': 'Task updated', 'data': self._get_one(id)}
        else:
            return {'error': 'Task not found'}

    def delete_task(self, id):
        task = self._get_one(id)
        if task:
            self.db.delete(task)
            self.db.commit()
            return {'info': 'Task deleted', 'data': self._get_all()}
        else:
            return {'error': 'Task not found'}