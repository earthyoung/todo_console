from todo_service import TodoService
from unittest.mock import patch
import pytest
from test_todo_application import todo_application


@pytest.fixture
def todo_service(todo_application):
    return TodoService(todo_application=todo_application)


def test_singleton(todo_service):
    todo_service_2 = TodoService(todo_application)
    assert todo_service == todo_service_2


def test_when_menu_input_is_invalid(todo_service, capsys):
    with patch("builtins.input", return_value=5):
        todo_service.run()
        result = capsys.readouterr()
        assert "[Exception] Invalid choice" in result.out
