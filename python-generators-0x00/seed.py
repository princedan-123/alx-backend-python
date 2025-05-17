"""
    A script that establishes a connection to Mysql database server
    and populates it with data from a csv file.
"""
import csv
import os
from mysql.connector import connect
from dotenv import load_dotenv

database = os.getenv('database')
password = os.getenv('password')
user = os.getenv('user')

def connect_db():
    """A Function that establishes connection to a Mysql server."""
    try:
        connection = connect(
        host='localhost',
        user=user,
        password=password,
        )
    except Exception as e:
        print('An error occured while trying to establish connection', e)
    return connection
    

def create_database(connection):
    """
    A function that creates a database.
    Arg: connection - a database connection.
    """
    with connection.cursor() as cursor:
        cursor.execute(
            """
            CREATE DATABASE IF NOT EXISTS ALX_prodev
            """
        )
        connection.commit()
    
def connect_to_prodev():
    """A function that establishes a connection and connects to a database."""
    db = connect(
        host='localhost',
        user=user,
        password=password,
        database=database
    )
    return db

def create_table(connection):
    """
    A function that creates a table if it does not exist.
    Arg: connection - a connection to a database.
    """
    with connection.cursor() as cursor:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) PRIMARY KEY DEFAULT(UUID()),
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL(10, 0) NOT NULL
            )
            """
        )
        connection.commit()

def insert_data(connection, data):
    """
    A function that inserts data into the ALX_prodev database.
    Args: connection - A connection to the database
          data - A csv file with data to populate the database
    Return: None
    """
    with open(data, newline='', encoding='utf-8') as file:
        file_iterator = csv.reader(file)
        next(file_iterator)
        with connection.cursor() as cursor:
            for row in file_iterator:
                name = row[0]
                email = row[1]
                age = row[2]
                cursor.execute(
                    """
                    INSERT INTO user_data (name, email, age)
                    VALUES(%s, %s, %s)
                    """,
                    (name, email, age)
                )
            connection.commit()
