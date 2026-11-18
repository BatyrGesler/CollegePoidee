from fastapi import FastAPI, HTTPException

app = FastAPI()

products = [
    {"id": 1, "name": "Milk", "price": 500},
    {"id": 2, "name": "Bread", "price": 200},
    {"id": 3, "name": "Eggs", "price": 800},
]


@app.get("/products")
def get_products(max_price: int = None):
    if max_price is not None:
        return [p for p in products if p["price"] <= max_price]
    return products


@app.get("/products/total")
def get_total():
    total = sum(p["price"] for p in products)
    return {"total": total, "count": len(products)}


@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")


@app.post("/products")
def add_product(name: str, price: int):
    new_product = {
        "id": len(products) + 1,
        "name": name,
        "price": price
    }
    products.append(new_product)
    return new_product