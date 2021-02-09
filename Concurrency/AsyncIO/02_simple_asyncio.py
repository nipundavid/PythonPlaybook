'''
asyncio implemented,
the time taken to make 3 calls of count()
is took ~1 second
'''
import time
import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    # await count()
    await asyncio.gather(count(), count(), count())

start = time.perf_counter()
asyncio.run(main())
elapsed = time.perf_counter() - start
print(f"executed in {elapsed:0.2f} seconds.")