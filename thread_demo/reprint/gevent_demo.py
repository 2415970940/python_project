# gevent   greenlet+异步IO
# pip install greenlet            pip install gevent
import gevent
import requests
from gevent import monkey
# 异步
monkey.patch_all()

def fetch_async(method,url,req_kwargs):
    print(method,url,req_kwargs)
    response = requests.request(method=method,url=url,**req_kwargs)
    print(response.status_code,response.url)

# gevent.joinall([
#     gevent.spawn(fetch_async,method='get',url='https://www.baidu.com/',req_kwargs={}),
#     gevent.spawn(fetch_async,method='get',url='https://www.python.org/',req_kwargs={}),
#     gevent.spawn(fetch_async,method='get',url='https://www.cnblogs.com/',req_kwargs={}),
# ])

# 发送请求（协程最多请求数）
from gevent.pool import Pool
pool = Pool(5)
gevent.joinall([
    pool.spawn(fetch_async,method='get',url='https://www.baidu.com/',req_kwargs={}),
    pool.spawn(fetch_async,method='get',url='https://www.python.org/',req_kwargs={}),
    pool.spawn(fetch_async,method='get',url='https://www.cnblogs.com/',req_kwargs={}),
])


# gevent+requests =>模块  grequests