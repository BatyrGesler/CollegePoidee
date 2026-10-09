from functools import reduce

products = [
    {"name": "Наушники", "price": 15000, "in_stock": True},
    {"name": "Веб-камера", "price": 20000, "in_stock": False},
    {"name": "Флешка", "price": 4000, "in_stock": True},
    {"name": "Коврик", "price": 3000, "in_stock": True},
]

fltr = list(filter(lambda p: p["in_stock"], products))

mapp = list(map(lambda p: p["price"] * 0.9, fltr))

reduc = reduce(lambda x, y: x + y, mapp, 0)

print(fltr)
print(mapp)
print(reduc)


