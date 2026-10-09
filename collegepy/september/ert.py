def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


while True:
    user_input = input("Enter a number (or 'exit' for exit): ")

    if user_input.lower() == "exit":
        break

    if user_input.isdigit():
        number = int(user_input)
        if is_prime(number):
            print(f"{number} - prostoe")
        else:
            print(f"{number} - ne prostoe")
    else:
        print("Please enter a number (or 'exit' for exit)")