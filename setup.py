# setup.py
from setuptools import setup

setup(
    name='dbtest',
    version='0.1',
    packages=['dbtest'],
    install_requires=[
        'dotenv',
        'unittest',
        'psycopg2-binary',
        'sqlalchemy',
        'pandas',
    ],
)