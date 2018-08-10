a=1
b="abc"

#type->int->1
print(type(a))
print(type(type(a)))
print(type(type(type(a))))
print(int.__base__)

print(type(b))
print(type(type(b)))

print("="*30)

class Person():
    pass

class Student(Person):
    pass

print(type(Student))
print(type(Person))
print(Student.__base__)
print(Person.__base__)
print(Person.__base__.__base__)
"""
<class 'type'>
<class 'type'>
<class '__main__.Person'>
<class 'object'>
None
"""
print("="*30)
# 总结：type生成所有类,包括object，所有类继承object
# type是个对象，也是个类
print(type.__base__)
print(type(type))
print(type(object))