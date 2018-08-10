class Company():
    def __init__(self,employee):
        self.employee = employee

    def __len__(self):
        return len(self.employee)



company = Company(["tom","bob","john"])
print(hasattr(company,"__len__"))
print(len(company))

# 判定对象类型
from collections.abc import Sized
print(isinstance(company,Sized))

"""
class Sized(metaclass=ABCMeta):

    __slots__ = ()

    @abstractmethod
    def __len__(self):
        return 0

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Sized:
            if any("__len__" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented
"""

# 使某个子类实现某个方法
# 需要设计抽象方法

# 如何实现抽象方法
# class CacheBase():
#     def get(self,key):
#         raise NotImplementedError
#     def set(self,key,value):
#         raise NotImplementedError
#
# class RedisCache(CacheBase):
#     # 不重写就会抛出异常
#     def set(self,key,value):
#         pass
#
# redis_demo = RedisCache()
# redis_demo.set("key","value")


# 跟上面一个例子的不同在于，上面set时才抛出异常，下面的是初始化的时候抛出异常
import abc
class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self,key):
        pass
    @abc.abstractmethod
    def set(self,key,value):
        pass

class RedisCache(CacheBase):
    def set(self,key,value):
        pass
    def get(self,key):
        pass

redis_demo = RedisCache()
redis_demo.set("key","value")