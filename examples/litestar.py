"""An example of a transformed FastAPI app to Litestar."""
from __future__ import annotations

from litestar import Litestar


@get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


@get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


# TODO: fix visitor and transforms
app = Litestar(**[read_root, read_item])
