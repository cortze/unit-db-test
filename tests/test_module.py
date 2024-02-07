import unittest
import unit_db_test.testcase as dbtest

config_files = ['.postgresql.env', '.clickhouse.env']


# test the different
for conf in config_files:
    class TestDBTestingModule(dbtest.DBintegrityTest):
        db_config_file = conf
        print(f"--> testing configuration file: {conf}")
        table_tag = ''
        if 'clickhouse' in conf:
            table_tag = 'default.'

        def test_not_null_items_in_column(self):
            # the query that SHOULDN'T create an assertion
            sql_query = f"""
            SELECT 
                id
            FROM {self.table_tag}test_table;        
            """
            df = self.db.get_df_from_sql_query(sql_query)
            self.assertNotNullItemsInColumn(df, 'id')

            # the query that SHOULD create the assertion raise
            sql_query = f"""
            SELECT 
                attribute_col
            FROM {self.table_tag}test_table;        
            """
            with self.assertRaises(AssertionError) as context:
                df = self.db.get_df_from_sql_query(sql_query)
                self.assertNotNullItemsInColumn(df, 'attribute_col')


        def test_custom_null_items_in_column(self):
            # the query that SHOULDN'T create an assertion
            sql_query = f"""
            SELECT 
                id
            FROM {self.table_tag}test_table;        
            """
            df = self.db.get_df_from_sql_query(sql_query)
            self.assertCustomNullItemsInColumn(df, 'id', 0)

            # the query that SHOULD create the assertion raise
            sql_query = f"""
            SELECT 
                attribute_col
            FROM {self.table_tag}test_table;        
            """

            df = self.db.get_df_from_sql_query(sql_query)
            with self.assertRaises(AssertionError) as context:
                self.assertCustomNullItemsInColumn(df, 'attribute_col', 3)
            self.assertCustomNullItemsInColumn(df, 'attribute_col', 1)

        def test_no_rows_assertion(self):
            # the query that SHOULDN'T create an assertion
            sql_query = f"""
            SELECT 
                id
            FROM {self.table_tag}test_table
            WHERE id=0;        
            """
            df = self.db.get_df_from_sql_query(sql_query)
            self.assertNoRows(df)

            # the query that SHOULD create the assertion raise
            sql_query = f"""
            SELECT 
                id
            FROM {self.table_tag}test_table
            WHERE id=1;       
            """

            df = self.db.get_df_from_sql_query(sql_query)
            with self.assertRaises(AssertionError) as context:
                self.assertNoRows(df)

        def test_custom_rows_assertion(self):
            # the query that SHOULDN'T create an assertion
            sql_query = f"""
            SELECT 
                attribute_col,
                count(attribute_col)
            FROM {self.table_tag}test_table
            GROUP BY attribute_col;        
            """
            df = self.db.get_df_from_sql_query(sql_query)
            self.assertNRows(df, 3)

            with self.assertRaises(AssertionError) as context:
                self.assertNRows(df, 4)


if __name__ == '__main__':
    unittest.main()