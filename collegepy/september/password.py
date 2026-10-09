password = input("Enter a password: ")

if password != password.lower():
    if len(password) > 8:
        for letter in password:
            if letter in "_1234567890@!#$%^&*":
                print("Molodec")
                exit(0)
            else:
                print("You must to write minimum one special symbol and number")
                exit(0)
    else:
        print("Password must be at least 8 characters long")
else:
    print("You must to write minimum one big letter")