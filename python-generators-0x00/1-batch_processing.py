"""
    A module that defines functions that fetch batch of users
    from a table in MySQL database.
"""
import os
from dotenv import load_dotenv
from mysql.connector import connect

load_dotenv()
user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')

def stream_users_in_batches(batch_size):
    """
        A function that streams data from a table in MySQL in batches.
        Arg: batch_size - the batch size of data to stream.
    """
    #  establish a connection with the database
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
            SELECT * FROM user_data LIMIT %s
            """,
            (batch_size,)
        )
        rows = cursor.fetchmany(batch_size)
        if len(rows) > 0:
            for row in rows:
                yield row
    except Exception as error:
        print(f'Error occured during batch streaming: {error}')
    finally:
        cursor.close()
        db.close()

def batch_processing(batch_size):
    """
        A function that processes each batch to filter out
        users over 25 year old.
        Arg: The size of each batch to be filtered.
    """
    output = []
    for row in stream_users_in_batches(batch_size):
        if row['age'] >= 25:
            print(row)
            output.append(row)
    return output
        
