"""This script implements a class based context manager."""
import sqlite3

class DatabaseConnection():
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
    def __enter__(self):
        return self.connection
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.connection.close()
        return True

with DatabaseConnection('users.db') as database_connection:
    cursor = database_connection.cursor()
    cursor.execute(
        """
        SELECT * FROM users;
        """
    )
    result = cursor.fetchall()
    print(result)