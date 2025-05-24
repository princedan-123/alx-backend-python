"""
    A script that implements a decorator that retries a database operation
    After a failure occurs.
"""
import time
import sqlite3 
import functools

def with_db_connection(func):
    """ your code goes here"""
    def wrapper(*args, **kwargs):
        connection = sqlite3.connect('users.db')
        try:
            results = func(connection, *args, **kwargs)
            return results
        finally:
            connection.close()
    return wrapper     

def retry_on_failure(retries=3, delay=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for retry in range(retries+1):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as error:
                    print(f'An error occured retrying operation')
                    print(f'retrying({retry})')
                if retry < retries:
                    time.sleep(delay)
            raise Exception('An error occured')
        return wrapper
    return decorator            

@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure
users = fetch_users_with_retry()
print(users)