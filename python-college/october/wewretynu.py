import sqlite3
from contextlib import closing

with closing(sqlite3.connect("school.db")) as conn:
    with conn:
        conn.execute("DROP TABLE IF EXISTS students")
        conn.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, group_name TEXT, mark INT)")
        name1 = "Osman"
        mark1 = 90
        name2 = "iskander"
        mark2 = 400
        group_name = "2508"

        conn.executemany(
            "INSERT INTO students (name, mark, group_name) VALUES (?, ?, ?)",
            [(name1, mark1, group_name), (name2, mark2, group_name)]
        )

        rows = [
            conn.execute("SELECT * FROM students WHERE name = ?", (name1,)).fetchall(),
            conn.execute("SELECT * FROM students WHERE name = ?", (name2,)).fetchall(),
        ]

print(rows)