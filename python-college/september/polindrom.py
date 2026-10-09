a = input("Write something: ")
c = ""
for s in a:
    if s in "!,.? ":
        continue
    else:
        c = c + s

b = c[::-1]

print(c)
print(b)
if c == b:
    print("Polindrom")
else:
    print("Not Polindrom")
