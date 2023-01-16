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
