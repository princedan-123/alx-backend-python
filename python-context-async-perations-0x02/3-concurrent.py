"""
Run multiple database queries concurrently using asyncio.gather.
"""
import aiosqlite
import asyncio

async def async_fetch_users():
    """A coroutine that fetches all users from the database."""
    connection = await aiosqlite.connect('users.db')
    cursor = await connection.execute(
        """
        SELECT * FROM users;
        """
    )
    result = await cursor.fetchall()
    print('printing all users')
    print(result)
    await cursor.close()
    await connection.close()

async def async_fetch_older_users():
    """A coroutine that fetches users older than 40."""
    connection = await aiosqlite.connect('users.db')
    cursor = await connection.execute(
        """
        SELECT * FROM users where age > ?;
        """, (40,)
    )
    result = await cursor.fetchall()
    print('printing older users')
    print(result)
    await cursor.close()
    await connection.close()

async def fetch_concurrently():
    """The main coroutine that serves as an entry point."""
    await asyncio.gather(async_fetch_users(), async_fetch_older_users())

asyncio.run(fetch_concurrently())
