class Author:
    def __init__(self, author_id, author_name):
        self.id = author_id
        self.name = author_name

    def __str__(self):
        return f"Author: {self.name} - ID: {self.id}"
