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
