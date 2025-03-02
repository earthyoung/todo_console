from todo import Todo
from typing import List
from datetime import datetime
from todo_application import TodoApplication


class TodoMemoryApplication(TodoApplication):

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(TodoMemoryApplication, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.todo_id: int = 1
        self.todos: List[Todo] = []
        self.created_at = datetime.now()

    def add(self, todo_title: str) -> Todo:
        todo = Todo(todo_title, self.todo_id)
        self.todos.append(todo)
        self.todo_id += 1
        return todo

    def remove(self, todo_id: int) -> None:
        todo_to_be_removed = self.get_todo_by_id(todo_id)
        if todo_to_be_removed is not None:
            self.todos.remove(todo_to_be_removed)
        else:
            print("[Exception] Todo not found")

    def list(self) -> List[Todo]:
        return self.todos

    def __str__(self) -> str:
        return self.created_at.isoformat()

    def get_todo_by_id(self, todo_id: int) -> Todo | None:
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None
