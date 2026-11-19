import asyncio

async def square(n):
    await asyncio.sleep(2)
    return n * n

async def main():
    result = await asyncio.gather(
        square(2), 
        square(3), 
        square(4)
    )
    print(result)

async def fn2():
    await asyncio.sleep(3)
    print("two")
    await asyncio.sleep(3)
    print("two")

async def main2():
    print("one")
    await asyncio.sleep(2)
    await fn2()
    
    print("three")
    await asyncio.sleep(2)
    await fn2()
    
    print("four")
    await asyncio.sleep(2)
    await fn2()
    
    print("five")
    await asyncio.sleep(2)
    await fn2()

asyncio.run(main())
asyncio.run(main2())
