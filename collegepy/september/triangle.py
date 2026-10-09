import random

a = random.randint(1, 100)
b = random.randint(1, 100)
c = random.randint(1, 100)

while a + b < c or b + c < a or c + a < b:
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    c = random.randint(1, 100)

print(a, b, c)
print(f"P = {a + b + c}")
