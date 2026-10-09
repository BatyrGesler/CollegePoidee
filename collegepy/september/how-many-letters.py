a = input("Enter string: ")
b = 0
symbols = ", .!?"

for i in a:
    if i not in symbols:
        b += 1
    else:
        continue

print(f"Letters in string: {b}")