import uuid

from app.likes.database import likes_database


class LikeAndUnlikeUseCase:
    database = likes_database

    async def create(self, reaction, user: str = None):
        return await self.database.create(
            {
                "post": reaction.post,
                "reaction": reaction.reaction,
                "user": user
            }
        )

    async def analitics_by_date(self, date_from, date_to):
        return await self.database.filter_by_date(date_from, date_to)
