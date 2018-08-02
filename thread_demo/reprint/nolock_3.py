# -*- coding: utf-8 -*-
#  导入相关依赖
import threading
import time

balance = 0 # 余额
def deposit(money):
    global balance
    balance += money

def excute_method(money):
    for i in range(100000):
        deposit(money)

t_1 = threading.Thread(name='t_1', target=excute_method, args=(1, ))
t_2 = threading.Thread(name='t_2', target=excute_method, args=(1, ))
t_1.start()
t_2.start()
t_1.join()
t_2.join()
print('balance is %s' % balance)