# 自省通过一定机制查询对象内部
class Person:
    name = "user"

class Student(Person):
    def __init__(self,college):
        self.college = college

stu = Student("hust")
print(stu.__dict__)
print(Student.__dict__)
print(Person.__dict__)
print("="*30)
print(dir(stu))
print(dir(Student))
print(dir(Person))