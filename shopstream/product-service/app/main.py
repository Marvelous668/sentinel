from fastapi import FastAPI, HTTPException

app = FastAPI(title="ShopStream Product Service")


products = [
    {
        "id": 1,
        "name": "Wireless Headphones",
        "price": 45000,
        "category": "Electronics",
    },
    {
        "id": 2,
        "name": "Mechanical Keyboard",
        "price": 35000,
        "category": "Electronics",
    },
    {
        "id": 3,
        "name": "USB-C Charger",
        "price": 12000,
        "category": "Accessories",
    },
]


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/products")
def get_products():
    return products


@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    raise HTTPException(status_code=404, detail="Product not found")
