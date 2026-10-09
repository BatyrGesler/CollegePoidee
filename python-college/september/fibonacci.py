a = int(input("Write number: "))
b = 0
c = 1
for i in range(a):
    b += c
    c = b -c

print(b)