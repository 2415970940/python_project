a = [1,2]
c = a + [3,4]
# c = a + (3,4) 报错
print(c)

from collections import abc
a += [5,6]
print(a)
a += (7,8)
print(a)
"""
+=
def __iadd__(self, values):
        self.extend(values)
        return self

def extend(self, values):
    'S.extend(iterable) -- extend sequence by appending elements from the iterable'
    for v in values:
        self.append(v)
"""

a.extend(range(3))
print(a)

a.append([11,33])
print(a)