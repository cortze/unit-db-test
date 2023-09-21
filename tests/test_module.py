import unittest
import unit_db_test.testcase as dbtest

class TestDBTestModule(dbtest.DBintegrityTest):
    db_config_file = '.env'

    def test_not_null_items_in_column(self):
        # the query that SHOULDN'T create an assertion
        sql_query = """
        SELECT 
            id
        FROM test_table;        
        """
        df = self.db.get_df_from_sql_query(sql_query)
        self.assertNotNullItemsInColumn(df, 'id')

        # the query that SHOULD create the assertion raise
        sql_query = """
        SELECT 
            attribute_col
        FROM test_table;        
        """
        with self.assertRaises(AssertionError) as context:
            df = self.db.get_df_from_sql_query(sql_query)
            self.assertNotNullItemsInColumn(df, 'attribute_col')

    def test_custom_null_items_in_column(self):
        # the query that SHOULDN'T create an assertion
        sql_query = """
        SELECT 
            id
        FROM test_table;        
        """
        df = self.db.get_df_from_sql_query(sql_query)
        self.assertCustomNullItemsInColumn(df, 'id', 0)

        # the query that SHOULD create the assertion raise
        sql_query = """
        SELECT 
            attribute_col
        FROM test_table;        
        """

        df = self.db.get_df_from_sql_query(sql_query)
        with self.assertRaises(AssertionError) as context:
            self.assertCustomNullItemsInColumn(df, 'attribute_col', 3)
        self.assertCustomNullItemsInColumn(df, 'attribute_col', 1)

    def test_no_rows_assertion(self):
        # the query that SHOULDN'T create an assertion
        sql_query = """
        SELECT 
            id
        FROM test_table
        WHERE id=0;        
        """
        df = self.db.get_df_from_sql_query(sql_query)
        self.assertNoRows(df)

        # the query that SHOULD create the assertion raise
        sql_query = """
        SELECT 
            id
        FROM test_table
        WHERE id=1;       
        """

        df = self.db.get_df_from_sql_query(sql_query)
        with self.assertRaises(AssertionError) as context:
            self.assertNoRows(df)

    def test_custom_rows_assertion(self):
        # the query that SHOULDN'T create an assertion
        sql_query = """
        SELECT 
            attribute_col,
            count(attribute_col)
        FROM test_table
        GROUP BY attribute_col;        
        """
        df = self.db.get_df_from_sql_query(sql_query)
        self.assertNRows(df, 3)

        with self.assertRaises(AssertionError) as context:
            self.assertNRows(df, 4)


if __name__ == '__main__':
    unittest.main()