from threading import Thread
class myThread(Thread):
    def __init__(self,name,user):
        self.user = user
        # super(myThread,self).__init__(name=name)
        super().__init__(name=name)

if __name__ == '__main__':
    a = myThread("a","mj")
    print(a)

# 涉及多继承时，super执行顺序是__mro__