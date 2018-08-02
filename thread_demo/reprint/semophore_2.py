import time
from random import random
from threading import Thread, Semaphore

sema = Semaphore(3)


def foo(tid):
    with sema:
        print ('{} acquire sema'.format(tid))
        wt = random() * 2
        time.sleep(wt)
    print ('{} release sema'.format(tid))


# threads = []
#
# for i in range(5):
#     t = Thread(target=foo, args=(i,))
#     threads.append(t)
#     t.start()
#
# for t in threads:
#     t.join()

# 上面创建了5个线程


from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor(3)

for i in range(5):
    pool.submit(foo,i)

pool.shutdown(wait=True)

