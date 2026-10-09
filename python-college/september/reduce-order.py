from functools import reduce

order = [
    {"name": "Клавиатура", "price": 12000},
    {"name": "Мышь", "price": 5500},
    {"name": "Монитор", "price": 89000},
]

sum_of_prices = reduce(lambda x, y: x + y, [item["price"] for item in order])
max_price = reduce(lambda x, y: x if x["price"] > y["price"] else y, order)

print(sum_of_prices)
print(max_price)