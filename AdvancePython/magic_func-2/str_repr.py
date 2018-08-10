# class Company():
#     def __init__(self,employee):
#         self.employee = employee
#
# company = Company(["tom","bob","john"])
# # print(str(company))
# print(company)


class Company():
    def __init__(self,employee):
        self.employee = employee

    def __str__(self):
        return ' '.join(self.employee)

company = Company(["tom","bob","john"])
print(company)
print(repr(company))
print(company.__repr__())