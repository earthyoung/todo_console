from todo_memory_application import TodoMemoryApplication
from todo_service import TodoService


def main():
    todo_application = TodoMemoryApplication()
    todo_service = TodoService(todo_application)
    todo_service.run()


if __name__ == "__main__":
    main()
