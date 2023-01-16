from typing import List, Union

from fastapi import APIRouter, status, Depends

from app.core.depends import get_current_user
from app.users.scheme import User

from app.likes import scheme as shm
from app.likes import service as srv

router = APIRouter()


@router.post("/", response_model=shm.LikeAndUnlike, status_code=status.HTTP_200_OK)
async def create_like_and_unlike(reaction: shm.LikeAndUnlike, user: User = Depends(get_current_user)):
    r =  await srv.LikeAndUnlikeUseCase().create(reaction, user=user.id)
    print("R!", r)
    return r
