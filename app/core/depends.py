from fastapi import Depends, HTTPException, status

from app.core import security as sec
from app.users.database import users_database
from app.users.scheme import User


async def get_current_user(
    token: str = Depends(sec.JWTBearer()),
) -> User:
    cred_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN, detail="Credentials are not valid"
    )
    payload = sec.decode_access_token(token)
    if payload is None:
        raise cred_exception
    email: str = payload.get("sub")
    if email is None:
        raise cred_exception
    user = await users_database.get_by_email(email=email)
    return cred_exception if user is None else user
