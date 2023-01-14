import datetime
from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from passlib.context import CryptContext

from app.core import config as cf

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hash_: str) -> bool:
    return pwd_context.verify(password, hash_)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    to_encode.update(
        {
            "exp": datetime.datetime.utcnow()
            + datetime.timedelta(minutes=cf.ACCESS_TOKEN_EXPIRE_MINUTES)
        }
    )
    return jwt.encode(to_encode, cf.JWT_SECRET_KEY, algorithm=cf.ALGORITM)


def decode_access_token(token: str):
    try:
        decode_jwt = jwt.decode(token, cf.JWT_SECRET_KEY, algorithms=[cf.ALGORITM])
    except jwt.JWSError:
        return None
    return decode_jwt


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        exp = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token")
        if credentials:
            token = decode_access_token(credentials.credentials)
            if token is None:
                raise exp
            return credentials.credentials
        else:
            raise exp
