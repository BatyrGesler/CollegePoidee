cipher = input()
step = int(input())
asd = ""
for i in cipher:
    if i in " ,.?!":
        continue
    else:
        g = ord(i)
        b = g + step
        if b > 122:
            b -= 26
        gg = chr(b)
        asd += gg

print(asd)
 
# print(ord("z"))