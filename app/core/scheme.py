import enum


class Collections(str, enum.Enum):
    """
    Collections names in MongoDB.
    """

    users: str = "users"
    posts: str = "posts"
    likes: str = "likes"
