dfgh = input()

grrr = 0
cd = 0
i = 0
while i < len(dfgh) - 1:
    if dfgh[i] == "C" and dfgh[i+1] == "D":
        grrr += 1
        if cd < grrr:
            cd = grrr
        i += 2
    else:
        grrr = 0
        i += 1

print(cd)