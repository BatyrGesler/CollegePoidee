import psycopg

with psycopg.connect(
    host="localhost",
    port=9432,
    dbname="new_base",
    user="BatosVopros",
    password="WubbaLubba",
) as conn:
    with conn.cursor() as cur:
        cur.execute("""DROP TABLE IF EXISTS sessions""")
        cur.execute("""CREATE TABLE IF NOT EXISTS sessions (id SERIAL PRIMARY KEY, movie TEXT, time TEXT, price INT, seats INT)""")
        cur.executemany("INSERT INTO sessions (movie, time, price, seats) values (%s,%s,%s,%s)",
                        [("Dune", "18:00", 1200, 15),
                         ("Avatar", "11:00", 1100, 21),
                         ("Michael", "15:00", 2200, 7),
                         ("Backrooms", "21:00", 2700, 12)])
        all = cur.execute("SELECT * FROM sessions").fetchall()
        print("Schedule:")
        for session in all:
            print(f"{session[2]} {session[1]} - {session[3]}, free seats: {session[4]}")

        cheap = cur.execute("SELECT * FROM sessions WHERE price < 1600").fetchall()
        print("cheaper than 1600:")
        for session in cheap:
            print(f"{session[1]} {session[3]}")

        cur.execute("UPDATE sessions SET seats = seats - 3 WHERE movie = 'Backrooms'")

        cur.execute("DELETE FROM sessions WHERE movie = 'Michael'")

        seats = cur.execute("SELECT seats FROM sessions").fetchall()
        total = 0
        for seat in seats:
            total += seat[0]

        print("Total free seats:", total)