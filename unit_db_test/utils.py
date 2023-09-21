# utils.py
import os
import os.path
from dotenv import load_dotenv

class NoEnvVariableError(Exception):
    def __init__(self, var_name: str):
        self.var = var_name

    def cause(self) -> str:
        return self.var


def load_credentials_from(file: str):
    check_if_exists(file)
    _ = load_dotenv(file)
    return get_db_credentials_from_env()


def check_if_exists(file: str):
    if not os.path.exists(file):
        raise FileNotFoundError(file)


def read_env_var(var_name: str):
    var = os.getenv(var_name)
    if var is None:
        raise NoEnvVariableError(var_name)
    else:
        return var


def get_db_credentials_from_env():
    user = read_env_var('DB_USER')
    password = read_env_var('DB_PASSWORD')
    host = read_env_var('DB_HOST')
    port = read_env_var('DB_PORT')
    database = read_env_var('DB_DATABASE')
    return user, password, host, port, database
