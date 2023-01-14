from typing import Union

import uvicorn
from fastapi import FastAPI

from app.users import api as api_users

app = FastAPI(title="Blog")

app.include_router(api_users.router, prefix="/api/users", tags=["users"])

@app.get("/")
def root_page():
    return {"hello": "world"}


if __name__ == "__main__":
    uvicorn.run(app, host=f"localhost", port=8000, log_level="debug")
