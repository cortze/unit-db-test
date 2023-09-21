# testcase.py
import pandas as pd
import unittest

from unit_db_test.postgresql import Postgres
from unit_db_test.utils import load_credentials_from



class DBintegrityTest(unittest.TestCase):
    db_config_file = ".env"

    # Initialization and configuration of the database
    def dbCredentials(self):
        """ replace this function at each unitt db integrity test with the db credentials """
        self.db_config_file = ".env"

    def readCredentialsFromEnv(self):
        return load_credentials_from(self.db_config_file)

    def connectDB(self, user, password, ip, port, db, url):
        self.db = Postgres(user=user, password=password, host=ip, port=port, database=db, url=url)

    # setup main function for the db connection
    def setUp(self):
        try:
            u, p, i, port, db, url = self.readCredentialsFromEnv()
            self.connectDB(u, p, i, port, db, url)
        except Exception as e:
            self.assertRaise(e)
            self.fail("unable to make connection to the DB")

    def setDown(self):
        self.db.close()

    # Extension of the pre-available assert-methods (Panda Oriented)
    def assertNotNullItemsInColumn(self, df: pd.DataFrame, column: str):
        nul_values = df[column].isnull().sum()
        if nul_values > 0:
            raise AssertionError(f"column {column} has {nul_values} null values, expected 0")

    def assertCustomNullItemsInColumn(self, df: pd.DataFrame, column: str, target: int):
        nul_values = df[column].isnull().sum()
        if nul_values != target:
            raise AssertionError(f"column {column} has {nul_values} null values, expected {target}")

    def assertNoRows(self, df: pd.DataFrame):
        self.assertNRows(df, 0)

    def assertNRows(self, df: pd.DataFrame, target_rows: str):
        if len(df) != target_rows:
            raise AssertionError(f"df has {len(df)} items, expected {target_rows}")

