from typing import List, Union

from fastapi import APIRouter, status
from app.users import scheme as shm
from app.users import service as srv

router = APIRouter()


@router.post("/", response_model=shm.UserOut, status_code=status.HTTP_201_CREATED)
async def singup_user(new_user: shm.UserIn):
    return await srv.SingupUser(new_user).create_user()


@router.post("/login/", response_model=shm.Token)
async def login_user(login: shm.Login):
    return await srv.LoginUser(login).login()
