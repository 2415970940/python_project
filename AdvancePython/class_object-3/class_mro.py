# C3算法
# class D:
#     pass
#
# class E:
#     pass
#
# class B(D):
#     pass
#
# class C(E):
#     pass
#
# class A(B,C):
#     pass
#
# print(A.__mro__)
# # (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.D'>, <class '__main__.C'>, <class '__main__.E'>, <class 'object'>)
# # A->B->D->C->E->object

class D:
    pass

class B(D):
    pass

class C(D):
    pass

class A(B,C):
    pass

print(A.__mro__)
# A->B->C->D