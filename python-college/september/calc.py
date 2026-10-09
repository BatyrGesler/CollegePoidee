# a = float(input("Enter 1st number: "))
# b = input("Enter operator: ")
# c = float(input("Enter 2nd number: "))
result = 0
while True:
    a = input("Enter 1st number: ")
    if a == "exit":
        print("You have exited")
        break
    b = input("Enter operator: ")
    if b == "exit":
        print("You have exited")
        break
    c = input("Enter 2nd number: ")
    if c == "exit":
        print("You have exited")
        break


    else:
        a = float(a)
        c = float(c)

        if b == "+":
            result = a + c
            print(result)
        elif b == "-":
            result = a - c
            print(result)
        elif b == "*":
            result = a * c
            print(result)
        elif b == "/":
            if c == 0:
                print("Cannot divide by zero")
                continue
            result = a / c
            print(result)
        else:
            print("Fignya")

