from typing import Union

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root_page():
    return {"hello": "world"}


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=f"localhost",
        port=8000,
        log_level="debug"
    )
