import time
import threading

def profile(func):
    def wrapped(*args,**kwargs):
        start =time.time()
        func(*args,**kwargs)
        end = time.time()
        print('cost:{}'.format(end-start))
    return wrapped

def fib(n):
    if n<2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

@profile
def nothread():
    fib(30)
    fib(30)

@profile
def hasthread():
    for i in range(2):
        t1 = threading.Thread(target=fib,args=(30,))
        t1.start()
    main_thread =threading.currentThread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        t.join()


if __name__ == '__main__':
    nothread()
    hasthread()

# cost:0.9446752071380615
# cost:0.9074094295501709

# 没有join（）
# cost:0.912628173828125
# cost:0.019035816192626953