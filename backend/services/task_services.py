from models.task_model import Task as TaskModel

class TaskService():
    def __init__(self, db) -> None:
        self.db = db

    def get_tasks(self):
        tasks = self.db.query(TaskModel).all()
        return tasks

    def get_done_task(self, id: int):
        task = self.db.query(TaskModel).filter(TaskModel.id == id).first()
        if task:
            if task.done:
                return False
            else:
                task.done = True
                self.db.commit()
                return True

        return None

    def get_undone_task(self, id: int):
        task = self.db.query(TaskModel).filter(TaskModel.id == id).first()
        if task:
            if not task.done:
                return False
            else:
                task.done = False
                self.db.commit()
                return True

        return None
      
    def get_all_done(self):
        tasks_undone = self.db.query(TaskModel).filter(TaskModel.done == False).all()

        if tasks_undone:
            for task in tasks_undone:
                task.done = True
            self.db.commit()
            return self.get_tasks()

        return None



    def get_task(self, id):
        task = self.db.query(TaskModel).filter(TaskModel.id == id).first()
        return task


    def create_task(self, task):
        self.db.add(task)
        self.db.commit()
        return task

    def update_task(self, id, task):    
        taskDB = self.get_task(id)
        if taskDB:
            taskDB.title = task.title
            taskDB.description = task.description
            taskDB.done = task.done
            self.db.commit()
            return self.get_task(id)
        else:
            return None
 

    def delete_task(self, id):
        task = self.get_task(id)
        if task:
            self.db.delete(task)
            self.db.commit()
            return self.get_tasks()
        else:
            return None