from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return {"welcome": "FastAPI"}


@app.get("/ping")
def read_root():
    return {"ping": "pong"}


@app.get("/pong")
def root_read():
    return {"pong": "ping"}

