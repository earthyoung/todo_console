from datetime import datetime


class Todo:
    def __init__(self, title: str, id: int):
        self.id = id
        self.title = title
        self.created_at = datetime.now()

    def __str__(self):
        return self.title
