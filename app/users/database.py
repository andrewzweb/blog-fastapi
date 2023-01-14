from app.core.database import Database
from app.core.scheme import Collections


class UserDatabase(Database):
    def __init__(self, collection=Collections.users):
        super().__init__(collection)

users_database = UserDatabase()
