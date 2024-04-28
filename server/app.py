import sys
from os import environ


with open(environ["LOG_FILE"], "a") as sys.stdout:
    print("Logging")

    from typing import Union

    from fastapi import FastAPI

    app = FastAPI()

    print("Python:Starting Server")

    @app.get("/")
    def read_root():
        return {"subject": environ}

    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}
