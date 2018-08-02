# -*- coding: utf-8 -*-
#  导入相关依赖
import threading
import time

lock = threading.Lock()
balance = 0

def deposit(money):
    global balance
    with lock:
    # balance += money
        temp = balance + money
        time.sleep(0.01) # 使线程有时间切换
        balance = temp

threads = []

for i in range(500):
    t = threading.Thread(target=deposit, args=(1, ))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
    print('balance is %s' % balance)

