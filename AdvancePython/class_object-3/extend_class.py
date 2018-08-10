a = ['a1','a2']
b = ['a1','a']

a.extend(b)
print(a)

class Company():
    def __init__(self,employee):
        self.employee = employee

    def __getitem__(self, item):
        return self.employee[item]



company = Company(["tom","bob","john"])
a.extend(company)
print(a)

# __getitem__使类可以迭代