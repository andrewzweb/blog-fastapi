from typing import Optional
from pydantic import BaseModel


class LikeAndUnlike(BaseModel):
    id: Optional[str]
    post: str
    reaction: bool # True - Like , False - Unlike
    user: Optional[str]
