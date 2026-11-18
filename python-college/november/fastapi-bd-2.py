import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
DB = "books.db"

def get_connection():
    return sqlite3.connect(DB)

conn = get_connection()
conn.execute("""CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, year INTEGER)""")
conn.commit()
conn.close()


class Book(BaseModel):
    title: str
    author: str
    year: int

@app.get("/books")
def get_books_by_author(author: str = None):
    conn = get_connection()
    if author:
        rows = conn.execute("SELECT id, title, author, year FROM books WHERE author = ?", (author,)).fetchall()
    else:
        rows = conn.execute("SELECT id, title, author, year FROM books").fetchall()
    conn.close()
    return [{"id": r[0], "title": r[1], "author": r[2], "year": r[3]} for r in rows]

@app.get("/books/{book_id}")
def get_book(book_id: int):
    conn = get_connection()
    row = conn.execute("SELECT id, title, author, year FROM books WHERE id = ?", (book_id,)).fetchone()
    conn.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"id": row[0], "title": row[1], "author": row[2], "year": row[3]}

@app.post("/books")
def add_book(book: Book):
    conn = get_connection()
    cur = conn.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (book.title, book.author, book.year))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return {"id": new_id, "title": book.title, "author": book.author, "year": book.year}

@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    conn = get_connection()
    cur = conn.execute("UPDATE books SET title = ?, author = ?, year = ? WHERE id = ?", (book.title, book.author, book.year, book_id))
    conn.commit()
    changed = cur.rowcount
    conn.close()
    if changed == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book updated"}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    conn = get_connection()
    cur = conn.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    changed = cur.rowcount
    conn.close()
    if changed == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted"}