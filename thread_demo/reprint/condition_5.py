# this is a bug
import threading
import time
import queue

condition = threading.Condition()
# 产品队列
products = queue.Queue(10)
count = 20 # 最多生产20个
# done = False  # 结束标志

class Producer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global condition, products, count, done
        while count > 0:
            if condition.acquire():
                while not products.full():
                    products.put(1)
                    print("Producer(%s):deliver one, now products count:%s" %(self.name, products.qsize()))
                    condition.notify()
                    count -= 1
                while products.full():
                    print("Producer(%s):already 10, stop deliver, now products:%s" %(self.name, 0))
                    condition.wait()
                    condition.release()
                    time.sleep(0.5)
                    # done = True
                    print('break producer')

class Consumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global condition, products, done
        # while not done:
        while True:
            if condition.acquire():
                while not products.empty():
                    n = products.get()
                    time.sleep(0.5)
                    print("Consumer(%s):consume one, now products:%s" % (self.name, n))
                    condition.notify()
                while products.empty():
                    print("Consumer(%s):only 0, stop consume, products:%s" % (self.name, 0))
                    condition.wait()
                    condition.release()
                    time.sleep(0.5)
                    print('break consumer')


threads = []

for p in range(0, 3):
    p = Producer()
    p.start()
    threads.append(p)

for c in range(0, 4):
    c = Consumer()
    c.start()
    threads.append(c)

for t in threads:
    t.join()

print('end main')

