from typing import Optional

from motor import motor_asyncio
from motor.motor_asyncio import AsyncIOMotorCollection

from app.core import config

client = motor_asyncio.AsyncIOMotorClient(config.MONGODB_URL)
mongodb = client[config.DATABASE_NAME]


class Database:
    def __init__(self, collection: str, database=mongodb):
        self.collection: AsyncIOMotorCollection = database[collection]

    def __call__(self):
        """For using as dependency in routes and overwriting in tests."""
        return self

    async def list(self, params: dict = None, skip: int = 0, limit: int = 20) -> list:
        cursor = self.collection.find(params or {}).skip(skip).limit(limit)
        return await cursor.to_list(length=limit)

    async def get(self, item: str) -> dict:
        return await self.collection.find_one({"id": item})

    async def create(self, data: dict, user: Optional[str] = None) -> dict:
        if user is not None:
            data["user"] = user
        result = await self.collection.insert_one(data)
        return await self.collection.find_one({"_id": result.inserted_id})

    async def update(self, item: str, data: dict) -> dict:
        await self.collection.update_one({"id": item}, {"$set": {**data}})
        return await self.collection.find_one({"id": item})

    async def delete(self, item: str) -> bool:
        result = await self.collection.delete_one({"id": item})
        return result.deleted_count > 0

    async def get_by_user(self, user: str, skip: int = 0, limit: int = 20):
        cursor = self.collection.find({"user": user}).skip(skip).limit(limit)
        return await cursor.to_list(length=limit)

    async def count(self):
        return await self.collection.count_documents({})
