
import asyncio

async def myfn():
    await # long code A

    # other codes B

async def myfn():
    task = asyncio.create_task(# long code A) 

    # other codes B

