import asyncio
from time import strftime


async def squarer(a):
    return a * a


async def doubler(x):
    return 2 * x


async def main(*args):
    res = await asyncio.gather((*squarer(arg) for arg in args))
    res = await asyncio.gather((*doubler(arg) for arg in args))
    print(*res)

asyncio.run(main(5, 9 , 0))
