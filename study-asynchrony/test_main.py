import asyncio
import time

async def one():
    print("Start one")
    await asyncio.sleep(1) # флаг- "я встаю на паузу, пусть поработает кто то другой"
    print("Stop one")

async def two():
    print("Start two")
    await asyncio.sleep(2) # здесь мы используем не обычные time sleep блокировку, а именно asyncio
    # await time.sleep(2) # так писать нельзя
    print("Stop two")

async def three():
    print("Start three")
    await asyncio.sleep(3)
    print("Stop three")


async def main():
    asyncio.create_task(one())
    asyncio.create_task(two())
    await asyncio.create_task(three())
    


start = time.time()
asyncio.run(main())
print(time.time() - start)
