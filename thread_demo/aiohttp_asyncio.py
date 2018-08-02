import asyncio
import aiohttp

@asyncio.coroutine
def func(url):
    response = yield from aiohttp.request('GET',url)
    print(url,response)
    response.close()


functions = [func("https://www.baidu.com/"),func("https://www.cnblogs.com/")]
# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
# loop.run_until_complete(func())
loop.run_until_complete(asyncio.gather(*functions))
loop.close()