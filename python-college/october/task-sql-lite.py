import sqlite3

from contextlib import closing


with closing(sqlite3.connect('lite.db')) as conn:
    with conn:
        conn.execute("DROP TABLE IF EXISTS musik")
        conn.execute("""CREATE TABLE IF NOT EXISTS musik (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        artist TEXT NOT NULL,
        likes INTEGER NOT NULL)""")

        conn.executemany("INSERT INTO musik (name, artist, likes) VALUES (?, ?, ?)",
                         [("Wrathchild", "Iron Maiden", 200),
                          ("No more tears", "Ozzy Osbourne", 400),
                          ("Life is killing me", "Type o Negative", 70),
                          ("Deutschland", "Rammstein", 430),
                          ("Die for your Government", "Anti-flag", 30)])

        print("----------------------------- 1 ---------------------------------")

        tracks = conn.execute("""SELECT * FROM musik""").fetchall()
        for track in tracks:
            print(f"{track[0]}. {track[1]}  - {track[2]} ({track[3]})")

        print("----------------------------- 2 ---------------------------------")
        tracks2 = conn.execute("""SELECT * FROM musik WHERE likes > 150 ORDER BY likes""").fetchall()
        for track in tracks2:
            print(f"{track[0]}. {track[1]}  - {track[2]} ({track[3]})")

        print("--------------------------- 3 ----------------------------------")
        conn.execute("""UPDATE musik SET likes = 999 where name = "No more tears" """)
        print(conn.execute("""SELECT * FROM musik WHERE name = "No more tears" """).fetchall())

        print("----------------------------- 4 ---------------------------------")
        conn.execute("""DELETE FROM musik WHERE name = "Die for your Government" """)

        tracks3 = conn.execute("""SELECT * FROM musik""").fetchall()
        for track in tracks3:
            print(f"{track[0]}. {track[1]}  - {track[2]} ({track[3]})")
