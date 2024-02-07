# postgresql.py
import pandas as pd
import psycopg2 as pspg
import sqlalchemy as sa


class  NoConnectionToDBError(Exception):
    def __init__(self, cause):
        self.cause = cause

    def cause(self):
        return self.cause

def parse_db_endpoint_string(s):
    driver = s.split(":")[0]
    user = s.split(":")[1].split("@")[0].split("//")[1]
    password = s.split(":")[2].split("@")[0]
    host = s.split(":")[2].split("@")[1]
    port = s.split(":")[3].split("/")[0]
    database = s.split(":")[3].split("/")[1]
    return driver, user, password, host, port, database


class SQLDatabase:
    def __init__(
        self,
        sql_driver: str,
        user: str,
        password: str,
        host: str,
        port: str,
        database: str,
    ):
        self.sql_driver = sql_driver
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.url = f"{sql_driver}://{user}:{password}@{host}:{port}/{database}"
        try:
            self.engine = sa.create_engine(url=self.url)
            self.conn = self.engine.connect()
        except pspg.OperationalError as dbError:
            raise NoConnectionToDBError(dbError)
        except Exception as e:
            raise NoConnectionToDBError(e)

    def get_df_from_sql_query(self, sql_query):
        return pd.read_sql_query(sa.text(sql_query), self.conn)

    def close(self):
        self.conn.close()
