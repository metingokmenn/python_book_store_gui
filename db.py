import sqlite3
from tkinter import messagebox as msg

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
        create table if not exists books (
            bid integer primary key autoincrement,
            bookname text,
            aid integer,
            FOREIGN KEY (aid) references authors(aid) 
        );
        """)
        self.cur.execute("""
        create table if not exists authors(
            aid integer primary key autoincrement,
            authorname text
        );  
        """)


        #self.cur.execute("""
        #select bid,bookname,authorname from (select bid,bookname,b.aid,authorname from books b, authors a where a.aid = b.aid)
        #
        #""")


        self.conn.close()

    def fill_database(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        data = [('Kitap adi', 'Yazar'),
                ('Yeni Kitap Adi', 'Yeni Yazar')]

        self.cur.execute("insert into authors(authorname) values('Refik Türker')")
        self.cur.execute("insert into books(bookname,aid) values('Küçük Prens', 1)")


        self.conn.commit()
        self.conn.close()

    def clear_database(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("delete from books")
        self.cur.execute("delete from authors")
        self.conn.commit()
        self.conn.close()

    def add_book(self, bookname, aid):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("insert into books(bookname, aid) values(:bookname, :aid)",
                    {"bookname": bookname,
                     "aid": aid})
        self.conn.commit()
        self.conn.close()

    def add_author(self, authorname):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("insert into authors(authorname) values(:authorname)",
                    {"authorname": authorname})
        self.conn.commit()
        self.conn.close()

    def list_books(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("select bid,bookname,authorname from (select bid,bookname,authorname from books b, authors a where b.aid = a.aid)")
        books = self.cur.fetchall()
        self.conn.close()
        return books

    def list_authors(self):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("select * from authors")
        authors = self.cur.fetchall()
        self.conn.close()
        return authors

    def delete_book(self, bid):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("delete from books where bid=?", [bid])
        self.conn.commit()

    def delete_author(self, aid):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("delete from authors where aid=?", [aid])
        self.cur.execute("delete from books where aid = ?", [aid])
        self.conn.commit()

    def edit_book(self, bid, bookname, aid):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("update books set bookname=?, aid=? where bid=?",
                         [bookname, aid, bid])
        self.conn.commit()

    def edit_author(self, aid, authorname):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("update authors set authorname=? where aid=?",
                         [authorname, aid])
        self.conn.commit()

    def get_max_book_id(self):
        conn = self.get_connection()
        cur = conn.cursor()

        cur.execute("SELECT MAX(bid) FROM books")
        max_book_id = cur.fetchone()[0]

        return max_book_id

    def search(self, search_key):
        conn = self.get_connection()
        cur = conn.cursor()

        cur.execute("select * from authors where authorname like ?", ['%' + search_key + '%'])
        searched_authors = cur.fetchall()
        cur.execute("select * from books where bookname like ?", ['%' + search_key + '%'])
        searched_books = cur.fetchall()
        searched_list = searched_authors + searched_books
        return searched_list

    def get_book_details(self, bid):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("""
            SELECT b.bid, b.bookname, a.aid, a.authorname
            FROM books b
            JOIN authors a ON b.aid = a.aid
            WHERE b.bid = ?
        """, [bid])
        book_details = self.cur.fetchone()
        self.conn.close()
        return book_details if book_details else None

    def get_author_details(self, aid):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()
        self.cur.execute("""
            SELECT a.aid, a.authorname, b.bid, b.bookname
            FROM authors a
            LEFT JOIN books b ON a.aid = b.aid
            WHERE a.aid = ?
        """, [aid])
        author_details = self.cur.fetchall()
        self.conn.close()
        return author_details if author_details else None

    def get_books_by_author(self, author_id):
        self.conn = self.get_connection()
        self.cur = self.conn.cursor()

        self.cur.execute("SELECT bid, bookname FROM books WHERE aid=?", [author_id])
        books = self.cur.fetchall()

        self.conn.close()
        return books

    def get_max_author_id(self):
        conn = self.get_connection()
        cur = conn.cursor()

        cur.execute("SELECT MAX(aid) FROM authors")
        max_book_id = cur.fetchone()[0]

        return max_book_id

    def get_authorname_by_aid(self, author_id):
        try:
            conn = self.get_connection()
            cur = conn.cursor()
            cur.execute("select authorname from authors where aid = ?", [author_id])
            author_name_tuple = cur.fetchall()
            author_name = author_name_tuple[0][0]
            return author_name
        except Exception as err:
            msg.showerror(title='Error', message='No author found by provided ID')



