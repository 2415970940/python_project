import asyncio
import requests

@asyncio.coroutine
def task(func,*args):
    loop = asyncio.get_event_loop()
    future = loop.run_in_executor(None,func,*args)
    response = yield from future
    print(response.url)


tasks = [task(requests.get,"https://www.baidu.com/"),task(requests.get,"https://www.cnblogs.com/")]
# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
# loop.run_until_complete(func())
loop.run_until_complete(asyncio.gather(*tasks))
loop.close()