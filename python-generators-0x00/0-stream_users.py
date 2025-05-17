"""
A script that fetches data from a Mysql database one at a time
using a generator function.
"""
import os
from mysql.connector import connect
from dotenv import load_dotenv

load_dotenv()
user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')

def stream_users():
    """ 
        A generator functions that streams data from a database one
        row at a time.
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
            """
            SELECT * FROM user_data;
            """
        )
        rows = cursor.fetchall()
        for row in rows:
            yield row
    except Exception as error:
        print(f'an error occured while trying to stream data: {error}')
    finally:
        cursor.close()
