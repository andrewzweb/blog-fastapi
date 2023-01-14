import uuid

from app.core import security as sec
from app.users import scheme as shm
from app.users.database import users_database


class LoginUser:
    database = users_database

    def __init__(self, data):
        self.email = data.email
        self.password = data.password

    async def login(self):
        user = await self.get_user_from_db()

        if not await self.check_user_exist(user):
            raise Exception("Incorrect username or password")

        if not await self.check_correct_password(user):
            raise Exception("Incorrect username or password")

        print(user)
        token = await self.create_token(user)
        return token

    async def get_user_from_db(self) -> "user":
        return  await database.get_by_email(self.email)

    async def check_user_exist(self, user) -> bool:
        if user is None:
            return False
        return True

    async def check_correct_password(self, user) -> bool:
        if not sec.verify_password(self.password, user.hashed_password):
            return False
        return True

    async def create_token(self, user):
        return shm.Token(
            access_token=sec.create_access_token({"sub": user.email}), token_type="Bearer")


class SingupUser:
    database = users_database

    def __init__(self, data: dict):
        self.data = data

    async def create_user(self):

        return await self.database.create(
            {
                "id": str(uuid.uuid4().hex),
                "username": self.data.username,
                "email": self.data.email,
                "hash_password": sec.hash_password(self.data.password)
            }

        )
