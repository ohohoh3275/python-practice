from fastapi import FastAPI

from typing import Optional
from pydantic import BaseModel
from .routers import enum


# it's like typescript :)
class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


app = FastAPI()
app.include_router(enum.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/fast/{id}")
def fast(id:int):
    return {"id":id}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}