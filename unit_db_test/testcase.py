# testcase.py
import pandas as pd
import unittest

from unit_db_test.postgresql import Postgres, NoConnectionToDBError
from unit_db_test.utils import load_credentials_from, NoEnvVariableError



class DBintegrityTest(unittest.TestCase):
    db_config_file = ".env"
    db = None

    # Initialization and configuration of the database
    @classmethod
    def dbCredentials(cls):
        """ replace this function at each unitt db integrity test with the db credentials """
        cls.db_config_file = ".env"

    @classmethod
    def readCredentialsFromEnv(cls):
        return load_credentials_from(cls.db_config_file)

    @classmethod
    def connectDB(cls, user, password, ip, port, db):
        cls.db = Postgres(user=user, password=password, host=ip, port=port, database=db)

    # setup main function for the db connection
    @classmethod
    def setUpClass(cls):
        try:
            u, p, i, port, db = cls.readCredentialsFromEnv()
            cls.connectDB(u, p, i, port, db)
        except NoEnvVariableError as envError:
            raise envError
        except NoConnectionToDBError as dbError:
            raise dbError

    @classmethod
    def setDownClass(cls):
        cls.db.close()

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

    def assertNRows(self, df: pd.DataFrame, target_rows: int):
        if len(df) != target_rows:
            raise AssertionError(f"df has {len(df)} rows, expected {target_rows}")

