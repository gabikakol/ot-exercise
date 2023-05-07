import os
from dotenv import load_dotenv

dir_name = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dir_name, "..", ".env"))
except FileNotFoundError:
    print("Environment file not found.")

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
DATABASE_FILEPATH = os.path.join(dir_name, "..", "data", DATABASE_FILENAME)
