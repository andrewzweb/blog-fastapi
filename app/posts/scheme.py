from pydantic import BaseModel


class PostIn(BaseModel):
    title: str
    description: str


class PostOut(BaseModel):
    id: str
    title: str
    description: str
    user: str
