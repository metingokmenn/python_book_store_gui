import sqlite3

class DatabaseManager:
    def __init__(self):
        self.conn = None
        self.cur = None

    @staticmethod
    def get_connection():
        return sqlite3.connect("booksandauthors.db")

    def create_database(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("""
        create table Book (
            bid   integer primary key autoincrement,
            bookname text,
            authorname text
        );
        """)
        self.fill_database()
        self.conn.commit()
        self.conn.close()

    def fill_database(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        data = [('Kitap adi', 'Yazar'),
                ('Yeni Kitap Adi', 'Yeni Yazar')]

        for item in data:
            self.cur.execute("insert into Book(bookname, authorname) values(?, ?)", item)

        self.conn.commit()
        self.conn.close()

    def clear_database(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("delete from Book")
        self.conn.commit()
        self.conn.close()

    def add_book(self, bookname, authorname):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("insert into Book(fname, lname) values(:bookname, :authorname)",
                    {"bookname": bookname,
                     "authorname": authorname})
        self.conn.commit()
        self.conn.close()

    def list_books(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("select * from Book")
        books = self.cur.fetchall()
        self.conn.close()
        return books

    def delete_book(self, bid):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("delete from Book where bid=?", [bid])
        self.conn.commit()

    def edit_book(self, bid, bookname, authorname):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("update Book set bookname=?, authorname=? where bid=?",
                         [bookname, authorname, bid])
        self.conn.commit()
