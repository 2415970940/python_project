a = ['a1','a2']
b = ['a1','a']

a.extend(b)
print(a)

"""
def extend(self, iterable): # real signature unknown; restored from __doc__
    #  L.extend(iterable) -> None -- extend list by appending elements from the iterable
    pass
"""

a_set = set()
a_set.add('a3')
a_set.add('a4')
a.extend(a_set)
print(a)

a_tuple = ('a5','a6')
a.extend(a_tuple)
print(a)