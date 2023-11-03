from fastapi import APIRouter, HTTPException
from db import tbl_orders, database
from typing import List
from models import Order, OrderIn

router = APIRouter()


@router.get("/")
async def home():
    return {"Home": "Home"}


@router.get("/orders/", response_model=List[Order])
async def read_orders():
    query = tbl_orders.select()
    return await database.fetch_all(query)


@router.post("/orders/", response_model=Order)
async def create_order(order: OrderIn):
    query = tbl_orders.insert().values(**order.dict())
    last_record_id = await database.execute(query)
    return {**order.dict(), "id": last_record_id}


@router.get("/orders/{order_id}", response_model=Order)
async def read_order(order_id: int):
    query = tbl_orders.select().where(tbl_orders.c.id == order_id)
    return await database.fetch_one(query)


@router.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: int, new_order: OrderIn):
    query = tbl_orders.update().where(tbl_orders.c.id == order_id).values(**new_order.dict())
    await database.execute(query)
    return {**new_order.dict(), "id": order_id}


@router.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    query = tbl_orders.delete().where(tbl_orders.c.id == order_id)
    await database.execute(query)
    return {'message': 'Order deleted'}
