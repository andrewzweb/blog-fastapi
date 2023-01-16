from app.core.database import Database
from app.core.scheme import Collections
from app.users import scheme as shm


class UserDatabase(Database):
    def __init__(self, collection=Collections.users):
        super().__init__(collection)

    async def get_by_email(self, email: str) -> dict:
        user = await self.collection.find_one({"email": email})
        if user is None:
            return None
        return shm.UserDB(**user)


users_database = UserDatabase()
