def convert_temp(g, to = ""):
    if to == "":
        return (g * 9 / 5) + 32
    elif to == "c":
        return (g - 32) * 5 / 9


cf = input("Write c or nothing: ")
if cf == "c" or cf == "":
    b = int(input("Write temperature: "))
    print(convert_temp(b, cf))
else:
    print("Please write c or nothing")