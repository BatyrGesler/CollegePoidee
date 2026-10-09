students = [
    ("Aigerim", 4.6), ("Bekzat", 3.2), ("Dana", 4.0),
    ("Yerlan", 2.8), ("Zhanna", 4.9),
]


fltr = list(map(lambda s: s[0], filter(lambda s: s[1] >= 4.0, students)))

print(fltr)

bad_fltr = list(map(lambda s: s[0], filter(lambda s: s[1] < 4.0, students)))

print(bad_fltr)