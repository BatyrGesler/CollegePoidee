import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
DB = "games.db"

def get_connection():
    return sqlite3.connect(DB)

conn = get_connection()
# conn.execute("""DROP TABLE IF EXISTS""")
conn.execute("""CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, rating INTEGER)""")
conn.commit()
conn.close()



class Game(BaseModel):
    name: str
    rating: int

@app.post("/games")
def add_game(game: Game):
    conn = get_connection()
    cur = conn.execute("INSERT INTO games (name, rating) VALUES (?, ?)", (game.name, game.rating))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return {"id": new_id, "name": game.name, "rating": game.rating}

@app.get("/games")
def get_games(min_rating: int = 0):
    conn = get_connection()
    rows = conn.execute("SELECT id, name, rating FROM games WHERE rating >= ?", (min_rating,)).fetchall()
    conn.close()
    return [{"id": r[0], "name": r[1], "rating": r[2]} for r in rows]