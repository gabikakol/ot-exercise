import os
from dotenv import load_dotenv

dir_name = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dir_name, "..", ".env"))
except FileNotFoundError:
    pass

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
DATABASE_FILEPATH = os.path.join(dir_name, "..", "data", DATABASE_FILENAME)

TRIPS_FILENAME = os.getenv("TRIPS_FILENAME") or "trips.sqlite"
TRIPS_FILEPATH = os.path.join(dir_name, "..", "data", TRIPS_FILENAME)
