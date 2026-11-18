import psycopg2
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

conn = psycopg2.connect(host="localhost", port="9433", dbname="postgres17", user="Batyr", password="1234")

cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY, title TEXT, author TEXT, year INTEGER)""")
conn.commit()
cur.close()


class Book(BaseModel):
    title: str
    author: str
    year: int

@app.get("/books")
def get_books(author: str = None):
    cur = conn.cursor()
    if author:
        cur.execute("SELECT id, title, author, year FROM books WHERE author = %s", (author,))
    else:
        cur.execute("SELECT id, title, author, year FROM books")
    rows = cur.fetchall()
    cur.close()
    return [{"id": r[0], "title": r[1], "author": r[2], "year": r[3]} for r in rows]

@app.get("/books/{book_id}")
def get_book(book_id: int):
    cur = conn.cursor()
    cur.execute("SELECT id, title, author, year FROM books WHERE id = %s", (book_id,))
    row = cur.fetchone()
    cur.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"id": row[0], "title": row[1], "author": row[2], "year": row[3]}

@app.post("/books")
def add_book(book: Book):
    cur = conn.cursor()
    cur.execute("INSERT INTO books (title, author, year) VALUES (%s, %s, %s) RETURNING id", (book.title, book.author, book.year))
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    return {"id": new_id, "title": book.title, "author": book.author, "year": book.year}

@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    cur = conn.cursor()
    cur.execute("UPDATE books SET title = %s, author = %s, year = %s WHERE id = %s", (book.title, book.author, book.year, book_id))
    conn.commit()
    changed = cur.rowcount
    cur.close()
    if changed == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book updated"}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id = %s", (book_id,))
    conn.commit()
    changed = cur.rowcount
    cur.close()
    if changed == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted"}