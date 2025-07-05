"""A script that generate users average age
without using mysql avg function.
"""
from dotenv import load_dotenv
import os
from mysql.connector import connect

load_dotenv()
user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')

def stream_user_ages():
    """A function that streams users age."""
    try:
        db = connect(
            host='localhost',
            user=user,
            password=password,
            database=database,
        )
        cursor = db.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT age FROM user_data; 
            """
        )
        for row in cursor:
            yield row['age']
    except Exception as error:
        print(
            f'An error occured while trying to retrieve age from database: {error}'
            )
    finally:
        cursor.close()
        db.close()
        

def average_age():
    """A function that calculates the average age of users without
       using the mysql avg function.
    """
    age_count = 0
    count = 0
    for age in stream_user_ages():
        age_count += age
        count += 1
    print(f'Average age of users: {age_count /count}')