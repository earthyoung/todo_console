from todo_memory_application import TodoMemoryApplication
import pytest
from datetime import datetime


@pytest.fixture
def todo_application():
    return TodoMemoryApplication()


@pytest.fixture(scope="function", autouse=True)
def todo_application_initialize(todo_application):
    todo_application.__init__()
    yield


def test_singleton(todo_application):
    todo_application_2 = TodoMemoryApplication()
    assert todo_application == todo_application_2


def test_add_todo(todo_application):
    todo_application.add("Buy groceries")
    assert len(todo_application.todos) == 1


def test_remove_todo(todo_application):
    todo_application.add("Buy groceries")
    todo_application.remove(1)
    assert todo_application.todos == []


def test_list_todos(todo_application):
    todo_application.add("Buy groceries")
    todo_application.add("Clean the house")
    assert len(todo_application.list()) == 2

    is_test_successful = True
    for todo in todo_application.list():
        if todo.title not in ["Buy groceries", "Clean the house"]:
            is_test_successful = False
            break
    assert is_test_successful


def test_list_todos_initialized(todo_application):
    assert todo_application.list() == []
    assert todo_application.todo_id == 1
    assert todo_application.created_at is not None
