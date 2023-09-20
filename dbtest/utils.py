# utils.py
import os
from dotenv import load_dotenv


def load_credentials_from(file):
    _ = load_dotenv(file)
    return get_db_from_env()


def get_db_from_env():
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    database = os.getenv('DB_DATABASE')
    url = os.getenv('DB_URL')
    return user, password, host, port, database, url
