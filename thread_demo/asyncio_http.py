# asyncio不能实现http，能实现tcp
# http是基于tcp，http有header

import asyncio

@asyncio.coroutine
def func(host,url):
    reader,writer = yield from asyncio.open_connection(host,80)

    request_header_content = """GET %s HTTP/1.0\r\nHOST:%s\r\n\r\n"""%(url,host,)
    request_header_content = bytes(request_header_content,encoding='utf-8')

    writer.write(request_header_content)
    yield from writer.drain()
    text = yield from reader.read()
    print(host,url,text)
    writer.close()


functions = [func('www.baidu.com','/'),func('www.cnblogs.com','/')]
# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
# loop.run_until_complete(func())
loop.run_until_complete(asyncio.gather(*functions))
loop.close()