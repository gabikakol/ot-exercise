import sqlite3
from tests.testing_env.test_config import TEST_DATABASE_PATH

def get_database_connection():
    connection = sqlite3.connect(TEST_DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection