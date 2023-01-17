from typing import List, Union
import datetime

from fastapi import APIRouter, status, Depends

from app.core.depends import get_current_user
from app.users.scheme import User
from app.likes import scheme as shm
from app.likes import service as srv

router = APIRouter()


@router.post("/", response_model=shm.LikeAndUnlike, status_code=status.HTTP_200_OK)
async def create_like_and_unlike(
    reaction: shm.LikeAndUnlike, user: User = Depends(get_current_user)
):
    return await srv.LikeAndUnlikeUseCase().create(reaction, user=user.id)


@router.get("/analitics/", response_model=List[shm.LikeAndUnlike])
async def analitics_likes(
    date_from: datetime.date = datetime.date.today() - datetime.timedelta(days=7),
    date_to: datetime.date = datetime.date.today(),
):
    date_from = datetime.datetime.fromordinal(date_from.toordinal())
    date_to = datetime.datetime.fromordinal(date_to.toordinal())

    return await srv.LikeAndUnlikeUseCase().analitics_by_date(date_from, date_to)
