from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any, Dict, Optional

app = FastAPI()

@app.get("/hello")
def read_hello() -> Dict[str, str]:
    """Returns a simple greeting."""
    return {"message": "Hello, world!"}

class EchoRequest(BaseModel):
    data: Any

@app.post("/echo")
def echo_data(request: EchoRequest) -> Dict[str, Any]:
    """Echoes back the posted data."""
    return {"echo": request.data}

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

@app.get("/items/{item_id}")
def get_item(item_id: int) -> Dict[str, Any]:
    """Returns a fake item by ID."""
    # In a real app, fetch from DB. Here, return a sample.
    return {
        "item_id": item_id,
        "name": f"Item {item_id}",
        "description": "A sample item.",
        "price": 9.99,
        "in_stock": True
    }

@app.post("/items")
def create_item(item: Item) -> Dict[str, Any]:
    """Creates a fake item (returns the posted data)."""
    return {"item": item.dict()}
