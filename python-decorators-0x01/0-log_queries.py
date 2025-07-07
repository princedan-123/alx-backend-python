"""A script that implemets a decorator that logs a query before executing it."""
import sqlite3
import functools
from datetime import datetime

#### decorator to lof SQL queries

""" YOUR CODE GOES HERE"""
def log_queries(func):
    """ A decorator function that extends
        a function by logging its query.
    """
    @functools.wraps(func)
    def wrapper(query):
        print(f'{datetime.now()}  >>> {query}')
        return func(query)
    return wrapper
        

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
print(users)
