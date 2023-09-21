# unit-db-test &middot; [![PyPI Release](https://img.shields.io/pypi/v/unit-db-test.svg)](https://pypi.org/project/unit-db-test/) ![](https://github.com/cortze/dbtest/actions/workflows/module_tests.yml/badge.svg) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Is your tool hard to debug? Would it be easier to check it at the DB level? 

This module is for you! **unit-db-test** is a Python tool for conducting database tests. It is a unittest wrapper focussed on making DB integrity tests.
As it is an extension over the `unittest.TestCase` it is easy to configure and easy to integrate with GitHub actions.



## Features

- It has an integrated connection to a Postgres Database: easily configurable using the `.env` file.
- Fully compatible with `SQLAlchemy` and `Pandas`: get a `pandas.Dataframe` out of any SQL query you want to test.
- Unit-test oriented: Check if the `pandas.Dataframe` output matches the expected values, or catch it when the test fails.

## Installation

You can install **dbtests** using pip:

```bash
pip install unit-db-test
```

## Usage
Here's how you can use dbtests in your projects:

1. Create a `./test` folder as with any other kind of `unittests` (it is in fact compatible with other `unittests` just make there is a connection to a Postgres DB), and create a `test-file`.
```shell
my-tool/
├── my-tool/
│   ├── __init__.py
│   ├── script_1.py
└── tests/
    ├── __init__.py
    └── test_script_1.py
```

2. Once the script is created, we need to import the dependencies:
```python
# test_script_1.py
# Dependencies
import unittest
from unit_db_test.testcase import DBintegrityTest
```

3. Create a `DBintegrityTest` as if it was a `unittest.TestCase`. It is important to define the path to the `.env` that keeps the Postgres DB credentials:
```python
class TestDBTestModule(DBintegrityTest):
    db_config_file = '.env'
```

4. Create as many `test` functions as pleased:
```python
    def test_not_null_items_in_column(self):
        # the query that SHOULDN'T create an assertion
        sql_query = """
        SELECT 
            id
        FROM test_table;        
        """
        df = self.db.get_df_from_sql_query(sql_query)
        self.assertNotNullItemsInColumn(df, 'id')

if __name__ == '__main__':
    unittest.main()
```

5. Run it as you please:
```shell
python -m unittest tests/test_script_1.py
```

The tests can be run locally or integrated with Github Actions. 
For more examples, please check:
- [Github Action example](https://github.com/cortze/unit-db-test/blob/main/.github/workflows/module_tests.yml)
- [Test example](https://github.com/cortze/unit-db-test/blob/main/tests/test_module.py)

## Custom Assert 
The **dbtest** module contemplates new assert functions over `pandas.Dataframe` objects. 
This way the result of a simple query can be easily checked with the standard `unittest` nomenclature.

The list of current Asserts is the following:
- assertNotNullItemsInColumn(self, df, column)
- assertCustomNullItemsInColumn(self, df, column, target)
- assertNoRows(self, df)
- assertNRows(self, df, target_rows)

There will be more to come (under demand most probably). Feel free to suggest new ones though!


## Contributing
If you want to contribute to this project, please follow these guidelines:

- Fork the repository
- Create a new branch
- Make your changes
- Submit a pull request
- Bugs and Issues

If you encounter any bugs or issues, please report them here.

## Contact
Author: Mikel Cortes ([@cortze](https://github.com/cortze))

Feel free to reach out if you have any questions or suggestions!

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/cortze/unit-db-test/blob/main/LICENSE) file for details.
