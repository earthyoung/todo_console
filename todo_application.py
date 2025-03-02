from todo import Todo
from typing import List
from abc import ABC, abstractmethod


class TodoApplication(ABC):

    @abstractmethod
    def add(self, todo_title: str) -> Todo:
        pass

    @abstractmethod
    def remove(self, todo_id: int) -> None:
        pass

    @abstractmethod
    def list(self) -> List[Todo]:
        pass

    @abstractmethod
    def get_todo_by_id(self, todo_id: int) -> Todo | None:
        pass
