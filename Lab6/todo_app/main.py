from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Create a GET ReST API with path parameters
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = Query(None)):  # Making 'q' optional directly here
    if q is not None:
        return {"item_id": item_id, "q": q}
    else:
        return {"item_id": item_id, "q": "No query parameter"}

# Create a GET ReST API with query parameters
@app.get("/items/")
def get_items(q: Optional[str] = None):
    return {"q": q}

# FIX: Add the missing decorator to register this as a route
@app.get("/items/{item_id}/query")  # <-- This line was missing
def read_item_with_query(item_id: int, q: Optional[str] = Query(None)):
    return {"item_id": item_id, "q": q or "No query parameter"}

# Pydantic model for the Item
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# In-memory database
items = {}

# POST operation
@app.post("/items/")
async def create_item(item: Item):
    item_id = str(len(items))
    items[item_id] = item
    return {"item_id": item_id, "item": item}

# PUT operation
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    if str(item_id) not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[str(item_id)] = item
    return {"item_id": item_id, "item": item}

# DELETE operation
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if str(item_id) not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[str(item_id)]
    return {"detail": "Item deleted"}
