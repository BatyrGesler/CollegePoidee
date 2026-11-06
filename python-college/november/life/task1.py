import sqlite3

from contextlib import closing

with closing(sqlite3.connect('pets.db')) as conn:
    with conn:
        conn.execute("""DROP TABLE IF EXISTS pets""")
        conn.execute("""create table pets (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, kind text, age INTEGER)""")
        conn.executemany("insert into pets (name, kind, age) values (?, ?, ?)",
                         [("Barsik", "cat", 3),
                          ("Multik", "cat", 4),
                          ("Kesha", "papagei", 2),
                          ("Sharik", "dog", 7),
                          ("Murka", "cow", 10)])
        all = conn.execute("select * from pets").fetchall()
        for pet in all:
            print(f"{pet[1]} ({pet[2]}) age: {pet[3]}")
        cats = conn.execute("select name from pets where kind = 'cat'").fetchall()
        print("Cats:")
        for cat in cats:
            print(cat[0])

        oldest = conn.execute("select * from pets order by age desc limit 1").fetchall()
        g = oldest[0]
        print(f"Oldest: {g[1]}, age: {g[3]}")

        conn.execute("update pets set age = age + 1 where name = 'Multik'")

        conn.execute("delete from pets where name == 'Kesha'")

        all = conn.execute("select * from pets").fetchall()
        for pet in all:
            print(f"{pet[1]} ({pet[2]}) age: {pet[3]}")
