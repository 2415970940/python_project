import time
class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day =day

    def __str__(self):
        return "%d-%d-%d"%(self.year,self.month,self.day)

class User:
    def __init__(self,birthday):
        self.__birthday = birthday
    def get_age(self):
        return time.gmtime().tm_year-self.__birthday.year

if __name__ == '__main__':
    user = User(Date(1984,1,1))
    age = user.get_age()
    print(age)
    print(user._User__birthday)

"""
双下划线__ 属性私有化
user._User__birthday 还是可以访问的
"""
