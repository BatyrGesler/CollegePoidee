import math as m
import datetime as dt
import random as r


g = []
for i in range(1,4):
    f = r.randint(1, 51)
    s = r.randint(1, 51)
    t = r.randint(1, 51)
    fo = r.randint(1, 51)
    fif = r.randint(1, 51)

    print("itteration -", i)
    print(f, s, t,fo, fif)


com = m.comb(50, 5)
time = dt.datetime.now()
print(f"combs - {com}")
print(f"now its - {time}")