class Author:
    def __init__(self, author_id, author_name, author_books):
        self.id = author_id
        self.name = author_name
        self.books = author_books

    def __str__(self):
        return f"Author: {self.name} - Books: {self.books} - ID: {self.id}"
