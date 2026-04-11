import os
import socket
from datetime import datetime, timezone

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="DevOps Demo API", version="1.0.0")


class Item(BaseModel):
    name: str
    price: float


@app.get("/")
def root():
    return {
        "serverHost": socket.gethostname(),
        "time": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}


@app.post("/items")
def create_item(item: Item):
    return {"created": True, "item": item}
