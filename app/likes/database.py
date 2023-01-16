from app.core.database import Database
from app.core.scheme import Collections


class LikesDatabase(Database):
    def __init__(self, collection=Collections.likes):
        super().__init__(collection)

    async def create(self, like: dict, user: str = None) -> dict:
        if user is not None:
            like["user"] = user

        exist = await self.collection.find_one({"post": like["post"]})

        if exist is not None:
            await self.collection.update_one({"post": like['post']}, {"$set": {**like}})
            return await self.collection.find_one({"post": like["post"]})
        else:
            result = await self.collection.insert_one(like)
            return await self.collection.find_one({"_id": result.inserted_id})


likes_database = LikesDatabase()
