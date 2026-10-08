import os

import httpx
from fastapi import FastAPI

app = FastAPI(title="ShopStream Search Service")

PRODUCT_SERVICE_URL = os.getenv(
    "PRODUCT_SERVICE_URL",
    "http://localhost:8001",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/search")
def search_products(q: str):
    response = httpx.get(f"{PRODUCT_SERVICE_URL}/products")

    products = response.json()

    results = [
        product
        for product in products
        if q.lower() in product["name"].lower()
    ]

    return {
        "query": q,
        "results": results,
    }