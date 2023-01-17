from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class LikeAndUnlike(BaseModel):
    id: Optional[str]
    post: str
    reaction: bool  # True - Like , False - Unlike
    user: Optional[str]
    dateUpdted: Optional[datetime]
    dateCreated: Optional[datetime]
