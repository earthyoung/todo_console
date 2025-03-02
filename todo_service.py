from todo import Todo
from todo_application import TodoApplication


class TodoService:

    # Singleton
    def __new__(cls, todo_application):
        if not hasattr(cls, "instance"):
            cls.instance = super(TodoService, cls).__new__(cls)
        return cls.instance

    def __init__(self, todo_application: TodoApplication):
        print("=====Todo Console Program=====")
        self.todo_application = todo_application

    def __del__(self):
        print("=====Goodbye=====")

    def run(self):
        while True:
            print("1. Add Todo")
            print("2. List Todos")
            print("3. Remove Todo")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add()
            elif choice == "2":
                self.list()
            elif choice == "3":
                self.remove()
            elif choice == "4":
                break
            else:
                print("[Exception] Invalid choice")
                break

    def add(self):
        todo_title = input("Enter todo title: ")
        if todo_title == "":
            print("[Exception] Title cannot be empty")
        else:
            self.todo_application.add(todo_title)
            print(f"Todo with title '{todo_title}' added successfully")

    def list(self):
        todos = self.todo_application.list()
        print("=====Todo List=====")
        for todo in todos:
            print(f"{todo.id}. {todo.title}")
        print("===================")

    def remove(self):
        try:
            todo_id = int(input("Enter todo id: "))
            self.todo_application.remove(todo_id)
        except ValueError:
            print("[Exception] please enter a valid integer id")
            return
        except Exception as e:
            print(f"[Exception] {e}")
            return
