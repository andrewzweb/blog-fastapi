import os

TESTING = os.environ.get("TESTING")

# mongo db
MONGODB_URL = os.environ.get("MONGODB_URL", default="mongodb://localhost:27017/test_database")
DATABASE_NAME = os.environ.get("DATABASE_NAME", default="DEV_BLOG")

# secret key for jwt
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", default="f8fe352a6dd5d6812415940d72d1892b9379560133e23ccdd51e7419f77ca244")
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", default=1440)
ALGORITM = "HS256"


# changes for test env
if TESTING:
    DATABASE_NAME = "TEST_BLOG"
