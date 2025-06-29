import sqlite3

conn = sqlite3.connect("library.db")
cur = conn.cursor()

# Set up the database
def init_db():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# CREATE
def add_book(title, author):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO books (title, author) VALUES (?, ?)", 
                (title, author))
    
    new_book_id = cur.lastrowid
    cur.execute("SELECT * FROM books WHERE id = ?", (new_book_id,))
    new_book = cur.fetchone()
    conn.commit()
    conn.close()

    print("Book added successfully!")
    return {
        "id": new_book[0],
        "title": new_book[1],
        "author": new_book[2],
    }

# READ
def view_books():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    books = cur.fetchall()
    conn.close()

    if not books:
        return "No books found in the database."
    
    return books

# UPDATE
def update_book(book_id, new_title, new_author):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("UPDATE books SET title = ?, author = ? WHERE id = ?", 
                (new_title, new_author, book_id))
    conn.commit()
    conn.close()

    print("Book updated successfully!")

# DELETE
def delete_book(book_id):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()

    print("Book deleted successfully!")
