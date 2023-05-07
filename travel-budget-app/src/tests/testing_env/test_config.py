import os
from dotenv import load_dotenv

dir_name = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dir_name, "..", "..", "..", ".env.test"))
except FileNotFoundError:
    pass

TEST_DATABASE_FILENAME = os.getenv("TEST_DATABASE_FILENAME") or "test_database.sqlite"
TEST_DATABASE_PATH = os.path.join(dir_name, "..", "..", "..", "data", TEST_DATABASE_FILENAME)
