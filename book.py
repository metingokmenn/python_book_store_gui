class Book:
    def __init__(self, book_id, book_name, author_id):
        self.id = book_id
        self.name = book_name
        self.author = author_id

    def __str__(self):
        return f"Book: {self.name} - Author: {self.author} - ID: {self.id}"
