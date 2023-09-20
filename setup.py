# setup.py
from setuptools import setup

setup(
    name='unit-db-test',
    version='0.1',
    packages=['unit_db_test'],
    install_requires=[
        'dotenv',
        'unittest',
        'psycopg2-binary',
        'sqlalchemy',
        'pandas',
    ],
)