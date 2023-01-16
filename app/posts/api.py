from typing import List, Union

from fastapi import APIRouter, status, Depends

from app.core.depends import get_current_user
from app.users.scheme import User

from app.posts import scheme as shm
from app.posts import service as srv

router = APIRouter()


@router.post("/", response_model=shm.PostOut, status_code=status.HTTP_201_CREATED)
async def create_post(new_post: shm.PostIn, user: User = Depends(get_current_user)):
    return await srv.PostUseCase().create(new_post, user=user.id)
