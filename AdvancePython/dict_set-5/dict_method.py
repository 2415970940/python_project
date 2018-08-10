a = dict({'name':'tom','age':34})

# # clear
# a.clear()
# print(a)

# copy shallow copy
c={"user1":{"name":"tom"},"user2":{"name":"bob"}}
d = c.copy()
print(d)
d['user1']['name'] = 'jane'
print(d)
print(c)

b = a.copy()
b['name'] = 'alex'
print(a)
print(b)

# fromkeys
new_list = ["name","age"]
# f = dict.fromkeys(new_list,{"wow":24})
f = dict.fromkeys(new_list,'wow')
print(f)

print("---"*30)
# get
print(a)
print(a['name'])
# print(a['school']) 报错
print(a.get('name'))
print(a.get('school'))

# items
for key,value in a.items():
    print(key,value)

# keys
for key in a.keys():
    print(key)

print("---"*30)
# setdefault
x = a.setdefault("name","anonymous")
print(x)
x = a.setdefault("user","anonymous")
print(x)
print(a)

# update
a.update({"user":"1231"})
print(a)
a.update(user="12")
print(a)
a.update([("user","67")])
print(a)
a.update((("user","7"),))
print(a)