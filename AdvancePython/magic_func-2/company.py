# 魔法函数就是数据模型
# class Company():
#     def __init__(self,employee):
#         self.employee = employee
#
# company = Company(["tom","bob","john"])
# print(company)
# employees = company.employee
# print(employees)
# for employee in employees:
#     print(employee)

#company是对象，有__getitem__，company是可迭代的，并是序列类型，可切片
class Company():
    def __init__(self,employee):
        self.employee = employee

    def __getitem__(self, item):
        return self.employee[item]



company = Company(["tom","bob","john"])
print(company[:2])
print(company.employee)
print(company)

for em in company:
    print(em)