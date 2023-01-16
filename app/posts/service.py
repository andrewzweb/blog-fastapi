import uuid

from app.posts.database import posts_database


class PostUseCase:
    database = posts_database

    async def create(self, new_post, user: str = None):
        return await self.database.create(
            {
                "id": str(uuid.uuid4().hex),
                "title": new_post.title,
                "description": new_post.description,
                "user": user
            }
        )

