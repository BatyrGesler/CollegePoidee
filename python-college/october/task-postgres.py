import psycopg

with psycopg.connect(
    host="localhost",
    port=9432,
    dbname="new_base",
    user="BatosVopros",
    password="WubbaLubba",
) as conn:
    with conn.cursor() as cur:
        cur.execute("""DROP TABLE IF EXISTS cart""")
        cur.execute("""CREATE TABLE IF NOT EXISTS cart (id SERIAL PRIMARY KEY, name TEXT NOT NULL, count INT NOT NULL, price INT NOT NULL)""")
        cur.executemany("INSERT INTO cart (name, count, price) VALUES (%s, %s, %s)", [("Milk", 3, 520), ("Bread", 2, 200), ("Rolton", 1, 320), ("Cola", 1, 700)])
        g = cur.execute("SELECT name, count, price FROM cart").fetchall()
        for i in g:
            print(f"{i[0]}: {i[1]} piece x {i[2]} tg = {i[2] * i[1]} tg")
        total = 0
        for i in g:
            total += i[2] * i[1]
        print("---------------------------------")
        print("TOTAL PRICE:", total, "tg")

        print(cur.execute("SELECT name, price FROM cart WHERE price = (SELECT MAX(price) FROM cart").fetchall())