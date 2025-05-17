"""A script that uses generator to simulate a pagination."""
from mysql.connector import connect
from dotenv import load_dotenv
import os

load_dotenv()
user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')

def paginate_users(page_size, offset):
    """
    A function that implements the pagination
    Args: page_size - The total size of rows per output
    offset - The number of rows to skip, 0 for nextpage
    """
    try:
        db = connect(
            host='localhost',
            user=user,
            password=password,
            database=database
            )
        cursor = db.cursor(dictionary=True)
        cursor.execute(
            """SELECT * FROM user_data LIMIT %s OFFSET %s""",
            (page_size, offset)
            )
        page = cursor.fetchall()
        return page
    except Exception as error:
        print('An error occured while trying to fetch data from db')
        return error
    finally:
        cursor.close()
        db.close() 

def lazy_paginate(page_size):
    """
        A generator function that implements pagination.
        Arg: page_size - The total row per page.
    """
    offset = 0
    users = paginate_users(page_size, offset)
    while users:
        yield users
        offset += page_size
        user = paginate_users(page_size, offset)