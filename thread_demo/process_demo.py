from concurrent.futures import ProcessPoolExecutor
import requests

def task(url):
    response = requests.get(url)
    # print(url,response)
    return response


def done(future,*args,**kwargs):
    result = future.result()
    print(result,args,kwargs)

url_list=['https://cn.bing.com/',
          'https://www.baidu.com/',
          'http://www.12306.cn/mormhweb/',
          'http://www.ityouknow.com/link.html',
          'https://www.cnblogs.com/',
]

if __name__ == '__main__':
    pool = ProcessPoolExecutor(3)
    for url in url_list:
        v = pool.submit(task,url)
        v.add_done_callback(done)

    pool.shutdown(wait=False)