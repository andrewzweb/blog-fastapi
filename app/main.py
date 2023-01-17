from typing import Union

import uvicorn
from fastapi import FastAPI

from app.users import api as api_users
from app.posts import api as api_posts
from app.likes import api as api_likes


app = FastAPI(title="Blog")

app.include_router(api_users.router, prefix="/api/users", tags=["users"])
app.include_router(api_posts.router, prefix="/api/posts", tags=["posts"])
app.include_router(api_likes.router, prefix="/api/likes", tags=["likes"])


@app.get("/")
def root_page():
    return {"hello": "world"}


if __name__ == "__main__":
    uvicorn.run(app, host=f"localhost", port=8000, log_level="debug")
