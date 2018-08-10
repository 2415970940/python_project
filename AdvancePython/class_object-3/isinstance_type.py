class A:
    pass

class B(A):
    pass

b = B()
print(isinstance(b,B))
print(isinstance(b,A))

print(type(A))
print(type(B))
print(type(b))
print(type(b) is B)
print(type(b) is A)

# isinstance会找到其继承关系
