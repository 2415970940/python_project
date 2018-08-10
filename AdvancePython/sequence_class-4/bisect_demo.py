import bisect
# 处理已排序的序列
# 二分查找
insert_list = []
bisect.insort(insert_list,4)
bisect.insort(insert_list,3)
bisect.insort(insert_list,5)
bisect.insort(insert_list,1)
bisect.insort(insert_list,2)
print(insert_list)
# insort = insort_right
# bisect = bisect_right
print(bisect.bisect_left(insert_list,3))
print(insert_list)
print(bisect.bisect(insert_list,4))