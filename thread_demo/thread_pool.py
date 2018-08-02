from concurrent.futures import ThreadPoolExecutor
import requests
# #################第一种方式#####################
# def task(url):
#     response = requests.get(url)
#     print(url,response)
#
# pool = ThreadPoolExecutor(5)
#
# url_list=['https://cn.bing.com/',
#           'https://www.baidu.com/',
#           'http://www.12306.cn/mormhweb/',
#           'http://www.ityouknow.com/link.html',
#           'https://www.cnblogs.com/',
#
# ]
#
# for url in url_list:
#     pool.submit(task,url)
#
# pool.shutdown(wait=True)


# #################第2种方式#####################
def task(url):
    response = requests.get(url)
    # print(url,response)
    return response

pool = ThreadPoolExecutor(2)

def done(future,*args,**kwargs):
    result = future.result()
    print(result,args,kwargs)

url_list=['https://cn.bing.com/',
          'https://www.baidu.com/',
          'http://www.12306.cn/mormhweb/',
          'http://www.ityouknow.com/link.html',
          'https://www.cnblogs.com/',

]

for url in url_list:
    v = pool.submit(task,url)
    v.add_done_callback(done)

pool.shutdown(wait=True)