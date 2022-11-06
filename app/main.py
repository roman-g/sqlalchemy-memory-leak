import sqlalchemy.ext.asyncio as sa_async
import asyncpg
import asyncio


async def sa_main():
    engine = sa_async.create_async_engine('postgresql+asyncpg://postgres:some_secret@postgresql:5432/postgres')
    while True:
        async with engine.begin():
            pass


async def asyncpg_main():
    connection = await asyncpg.connect('postgresql://postgres:some_secret@postgresql:5432/postgres')
    while True:
        async with connection.transaction():
            pass


asyncio.run(sa_main())