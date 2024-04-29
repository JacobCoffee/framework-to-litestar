from litestar import get

from typing import Union

from fastapi import middleware, FastAPI

app = Litestar()


@get("/")
def read_root():
    return {"Hello": "World"}


@get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
