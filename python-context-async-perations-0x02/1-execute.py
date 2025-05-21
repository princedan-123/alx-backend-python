"""
A script that creates a reusable context manager that takes a query 
as input and executes it,
managing both connection and the query execution.
"""
import sqlite3

class ExecuteQuery():
    def __init__(self, database, query, parameter):
        self.connection = sqlite3.connect(database)
        self.query = query
        self.parameter = parameter
    def __enter__(self):
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query, (self.parameter,))
        return self.cursor
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.connection.close()
        return True

with ExecuteQuery('users.db','SELECT * FROM users WHERE age > ?', 25) as result:
    print(result.fetchall())