from collections import abc
import numbers
class Group:
    def __init__(self,group,company,staffs):
        self.group = group
        self.company = company
        # staffs is a list
        self.staffs = staffs

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False

    def __reversed__(self):
        self.staffs.reverse()

    def __len__(self):
        return len(self.staffs)
    # def __getitem__(self, item):
    #     return self.staffs[item]

    def __getitem__(self, item):
        cls=type(self)
        if isinstance(item,slice):
            return cls(group=self.group,company=self.company,staffs=self.staffs[item])
        elif isinstance(item,numbers.Integral):
            return cls(group=self.group,company=self.company,staffs=[self.staffs[item]])


    def __iter__(self):
        return iter(self.staffs)

if __name__ == '__main__':
    group = Group('A','ibm',['jane','tom','bob'])
    print(group.staffs[:2])
    sub_group = group[:2]
    print(sub_group)
    print(sub_group.staffs)
    sub_group1 = group[2]
    print(sub_group1)
    print(sub_group1.staffs)
    group.staffs.reverse()
    print(group.staffs)