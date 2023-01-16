from pydantic import BaseModel


class Login(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class UserIn(BaseModel):
    username: str
    email: str
    password: str
    password2: str


class User(BaseModel):
    username: str
    email: str
    password: str


class UserDB(BaseModel):
    id: str
    username: str
    email: str
    hashed_password: str


class UserOut(BaseModel):
    id: str
    username: str
    email: str
