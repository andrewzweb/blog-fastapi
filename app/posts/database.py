from app.core.database import Database
from app.core.scheme import Collections


class PostsDatabase(Database):
    def __init__(self, collection=Collections.posts):
        super().__init__(collection)

posts_database = PostsDatabase()
