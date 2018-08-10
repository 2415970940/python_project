class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day =day

    def __str__(self):
        return "%d-%d-%d"%(self.year,self.month,self.day)

    @staticmethod
    def parse_date_string(date_str):
        year,month,day = date_str.split("-")
        return Date(int(year),int(month),int(day))

    @classmethod
    def from_str(cls,date_str):
        year,month,day = date_str.split("-")
        return cls(int(year),int(month),int(day))



date = Date(2018,8,8)
print(date)

date_str = "2018-9-1"
# year,month,day = date_str.split("-")
# print(year,month,day)
print(Date.parse_date_string(date_str))
print(Date.from_str(date_str))



"""
实例方法
静态方法：@staticmethod  硬编码
类方法：@classmethod

静态方法不需要调用类
"""