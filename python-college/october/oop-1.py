class Product:
    def __init__(self, name, price, stock):
        if price < 0:
            raise ValueError("Price cannot be < 0")
        if stock < 0:
            raise ValueError("Stock cannot be < 0")
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} — {self.price:.2f} tenge (stock: {self.stock})"


class Cart:
    def __init__(self):
        self.items = []
    

    def _find(self, product_name):
        for item in self.items:
            if item["product"].name == product_name:
                return item
        return None

    def add(self, product, qty):
        if qty <= 0:
            raise ValueError("Quantity must be positive")

        item = self._find(product.name)
        already_in_cart = item["qty"] if item else 0

        if already_in_cart + qty > product.stock:
            raise ValueError(
                f"Not enough product «{product.name}» in stock: "
                f"available {product.stock}, requested {already_in_cart + qty}"
            )

        if item:
            item["qty"] += qty
        else:
            self.items.append({"product": product, "qty": qty})

    def remove(self, product_name):
        item = self._find(product_name)
        if item is None:
            raise ValueError(f"Product «{product_name}» is not in the cart")
        self.items.remove(item)

    def total(self):
        return sum(i["product"].price * i["qty"] for i in self.items)

    def checkout(self):
        for item in self.items:
            if item["qty"] > item["product"].stock:
                raise ValueError(
                    f"Not enough product «{item['product'].name}» in stock"
                )
        receipt = str(self)
        for item in self.items:
            item["product"].stock -= item["qty"]
        self.items.clear()
        return receipt

    def __len__(self):
        return len(self.items)

    def __str__(self):
        if not self.items:
            return "Cart is empty"
        text = "=" * 40 + "\n"
        text += "RECEIPT\n"
        text += "=" * 40 + "\n"
        for i in self.items:
            p, q = i["product"], i["qty"]
            text += f"{p.name:<15} {p.price:>8.2f} x {q:<3} = {p.price * q:>9.2f}\n"
        text += "-" * 40 + "\n"
        text += f"{'TOTAL:':<28}{self.total():>11.2f}\n"
        text += "=" * 40
        return text


products = [
    Product("Laptop", 55000, 5),
    Product("Mouse", 800, 10),
    Product("Телифон", 30000, 2),
]

cart = Cart()


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number")


def show_products():
    print("\nProducts:")
    number = 1
    for p in products:
        print(f"{number}. {p}")
        number += 1


def choose_product():
    show_products()
    number = read_int("Product number: ")
    if 1 <= number <= len(products):
        return products[number - 1]
    print("No such product")
    return None


while True:
    print("\n--- MENU ---")
    print("1. Show products")
    print("2. Add to cart")
    print("3. Remove from cart")
    print("4. Show cart")
    print("5. Checkout")
    print("0. Exit")

    choice = input("Choose action: ").strip()

    if choice == "1":
        show_products()

    elif choice == "2":
        product = choose_product()
        if product:
            qty = read_int("Quantity: ")
            try:
                cart.add(product, qty)
                print("Added to cart")
            except ValueError as e:
                print("Error:", e)

    elif choice == "3":
        name = input("Product name to remove: ").strip()
        try:
            cart.remove(name)
            print("Removed from cart")
        except ValueError as e:
            print("Error:", e)

    elif choice == "4":
        print(cart)
        print("Items in cart:", len(cart))

    elif choice == "5":
        if len(cart) == 0:
            print("Cart is empty")
        else:
            try:
                print(cart.checkout())
                print("Thank you for your purchase!")
            except ValueError as e:
                print("Error:", e)

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Unknown action, try again")