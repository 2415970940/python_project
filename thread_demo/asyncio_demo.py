import asyncio

@asyncio.coroutine
def func():
    print("before func...")
    # 异步调用asyncio.sleep(1):
    yield from asyncio.sleep(1)
    print("after func...")

functions = [func(),func()]
# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
# loop.run_until_complete(func())
loop.run_until_complete(asyncio.gather(*functions))
loop.close()