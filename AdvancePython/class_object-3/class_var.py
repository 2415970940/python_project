class A:
    aa=1
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'x:%d,y:%d,self.aa:%d,A.aa:%d'%(self.x,self.y,self.aa,A.aa)

a = A(4,5)
print(a)
A.aa = 2
a.aa = 100
print(a)

"""
aa是类变量，
类A实例化a时，给对象a新建一个aa变量，即实例化变量，
a查询顺序是，对象先在a.aa中找，没有则到A.aa找
"""