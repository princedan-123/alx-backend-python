import sqlite3
import functools
"""
    create a decorator that manages
    database transactions by automatically committing or rolling back changes
"""
def with_db_connection(func):
    """A decorator that creates a database connection"""
    def wrapper(*args, **kwargs):
        try:
            connection = sqlite3.connect('users.db')
            results = func(connection, *args, **kwargs)
            return results
        finally:
            connection.close()
    return wrapper

def transactional(func):
    """A decorator that wraps a function in a transcation."""
    def wrapper(connection, *args, **kwargs):
        """A wrapper function that extends the main function."""
        try:
            connection.execute('BEGIN')
            func(connection, *args, **kwargs)
            connection.commit()
        except Exception as error:
            connection.rollback()
    return wrapper


@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
    #### Update user's email with automatic transaction handling

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')