from fastapi import APIRouter, HTTPException
from db import tbl_products, database
from typing import List
from models import Product, ProductIn

router = APIRouter()


@router.get("/")
async def home():
    return {"Home": "Home"}


@router.get("/products/", response_model=List[Product])
async def read_products():
    query = tbl_products.select()
    return await database.fetch_all(query)


@router.post("/products/", response_model=Product)
async def create_product(product: ProductIn):
    query = tbl_products.insert().values(**product.dict())
    last_record_id = await database.execute(query)
    return {**product.dict(), "id": last_record_id}


@router.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: int):
    query = tbl_products.select().where(tbl_products.c.id == product_id)
    return await database.fetch_one(query)


@router.put("/products/{product}", response_model=Product)
async def update_product(product_id: int, new_product: ProductIn):
    query = tbl_products.update().where(tbl_products.c.id == product_id).values(**new_product.dict())
    await database.execute(query)
    return {**new_product.dict(), "id": product_id}


@router.delete("/products/{product_id}")
async def delete_product(product_id: int):
    query = tbl_products.delete().where(tbl_products.c.id == product_id)
    await database.execute(query)
    return {'message': 'Product deleted'}
