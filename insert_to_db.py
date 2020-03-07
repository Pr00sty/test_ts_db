import asyncio
import os
from typing import List
from logging import INFO, getLogger, basicConfig

LOGGER = getLogger()
basicConfig(level=INFO)

data_dir = "data/"


def list_data_files():
    return os.listdir(data_dir)


async def get_data_from_file(filename: str) -> List:
    with open(filename) as f:
        return f.readlines()


async def insert_date_to_db(filename: str):
    for line in await get_data_from_file(filename):
        print("{}: {}".format(filename, line))
        await asyncio.sleep(1)


async def main():
    list_of_async_tasks = []
    for file in list_data_files():
        list_of_async_tasks.append(asyncio.ensure_future(insert_date_to_db('{}/{}'.format(data_dir, file))))
    await asyncio.gather(*list_of_async_tasks)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
