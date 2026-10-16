from datetime import datetime as dt

cart = []
stock = {
    1: 'Маргарита',
    2: 'Пепперони',
    3: 'Мясная'
}


def log_action(message):
    now = dt.now()
    time = now.strftime('%Y-%m-%d %H:%M:%S')
    with open('in.txt', mode='a', encoding='utf-8') as f:
        print(time, " ", message, file=f)


def pizza(choice):
    cart.append(stock[choice])
    log_action('Пользователь добавил позицию в корзину\n')


def deleting():
    while True:
        ask = input("Do you want to delete something? [yes/no]: ")

        if ask == 'yes':
            log_action("User wants to delete something\n")
            print("=============================================")

            while True:
                delet = int(input(f'What do you want to delete? \n{cart} \nEnter 0 for exit \n'))

                if delet == 0:
                    log_action("User stoped deleting\n")
                    break
                deleted = cart.pop(delet - 1)

                print(f"you have deleted {deleted}")
                log_action(f"User deleted {deleted}\n")
                print("----------------------------------------------")

            print("your cart:", cart)
            break

        elif ask == 'no':
            print(f"ok your cart: {cart}")
            log_action("User didnt delete anything\n")
            break

        else:
            print("pls write yes or no")


print('=============================')
log_action('Пользователь запустил программу\n')
while True:
    choice = int(input('\nВыберите пиццу: \n1. Маргарита \n2. Пепперони \n3. Мясная \n0. Выход\n9. Deleting \n'))
    if choice == 9:
        deleting()
    if choice == 0:
        log_action('Пользователь завршил сессию\n')
        break
    if choice != 9:
        pizza(choice)


print("your cart:", cart)

