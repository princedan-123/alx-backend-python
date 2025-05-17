"""
A script that fetches data from a Mysql database one at a time
using a generator function.
"""
from seed import connect_to_prodev
def stream_users():
    """ 
        A generator functions that streams data from a database one
        row at a time.
    """
    try:
        db = connect_to_prodev()
        cursor = db.cursor()
        cursor.execute(
            """
            SELECT * FROM user_data;
            """
        )
        row = cursor.fetchone
        while row is not None:
            yield row
            row = cursor.fetchone
    except Exception as error:
        print(f'an error occured while trying to stream data: {error}')
    finally:
        cursor.close()
