"""
Esta clase modela una Tarea (Task).
"""
from uuid import UUID
from dataclasses import dataclass

@dataclass
class Task:
    id: UUID
    title: str
    description: str
    completed: bool = False
