# 列表生成式（列表推导式）
odd_list=[]
# for i in range(21):
#     if i%2 == 1:
#         odd_list.append(i)

# 列表生成式
odd_list = [i for i in range(21) if i%2 == 1 ]
print(type(odd_list))
print(odd_list)

def square_item(item):
    return item*item
odd_list = [square_item(i) for i in range(21) if i%2 == 1 ]
print(odd_list)
print("="*30)

# 生成器表达式
odd_gen = (i for i in range(21) if i%2 == 1 )
print(type(odd_gen))
print(odd_gen)

odd_list = list(odd_gen)
print(type(odd_list))
print(odd_list)
print("="*30)

# 字典推导式
my_dict = {'jane':21,'tom':12,'bob':30}
reversed_dict = {value:key for key,value in my_dict.items()}
print(reversed_dict)
print("="*30)

# 集合推导式
my_set = {key for key,value  in my_dict.items()}
print(type(my_set))
print(my_set)