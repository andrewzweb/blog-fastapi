import datetime
import uuid

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
            like["dateUpdted"] = datetime.datetime.now()
            await self.collection.update_one({"post": like["post"]}, {"$set": {**like}})
            return await self.collection.find_one({"post": like["post"]})
        else:
            like["id"] = str(uuid.uuid4().hex)
            like["dateUpdted"] = datetime.datetime.now()
            like["dateCreated"] = datetime.datetime.now()
            result = await self.collection.insert_one(like)
            return await self.collection.find_one({"_id": result.inserted_id})

    async def filter_by_date(self, date_from, date_to, skip=0, limit=20) -> dict:

        cursor = (
            self.collection.find({"dateCreated": {"$gte": date_from, "$lt": date_to}})
            .skip(skip)
            .limit(limit)
        )

        return await cursor.to_list(length=limit)


likes_database = LikesDatabase()
