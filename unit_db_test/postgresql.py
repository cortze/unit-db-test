# postgresql.py
import pandas as pd
import sqlalchemy as sa


def parse_db_endpoint_string(s):
    user = s.split(":")[1].split("@")[0].split("//")[1]
    password = s.split(":")[2].split("@")[0]
    host = s.split(":")[2].split("@")[1]
    port = s.split(":")[3].split("/")[0]
    database = s.split(":")[3].split("/")[1]
    return user, password, host, port, database


class Postgres:
    def __init__(
        self,
        port=None,
        user=None,
        password=None,
        database=None,
        host="localhost",
        url=None,
    ):
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        if url is not None:
            self.engine = sa.create_engine(url=url)
        else:
            self.url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
            self.engine = sa.create_engine(url=url)
        self.conn = self.engine.connect()

    def get_df_from_sql_query(self, sql_query):
        return pd.read_sql_query(sa.text(sql_query), self.conn)

    def close(self):
        self.conn.close()
