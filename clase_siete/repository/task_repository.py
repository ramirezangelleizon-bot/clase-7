"""
Esta clase manipula los datos.
"""
import uuid
from model.task import Task

class TaskRepository:
    def __init__(self):
        self._tasks: list[Task] = []

    def get_all(self) -> list[Task]:
        return self._tasks

    def create_one(self, title: str, description: str) -> Task:
        # ID único
        new_id = uuid.uuid4()
        new_task = Task(id=new_id, title=title, description=description)
        self._tasks.append(new_task)
        return new_task