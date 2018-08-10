class Cat(object):
    def say(self):
        print('i m a cat')

class Dog(object):
    def say(self):
        print('i m a dog')

class Duck(object):
    def say(self):
        print('i m a duck')

animal = Cat()
animal.say()
# 隐含他们有共同的方法，从而实现多态
animal_list = [Cat,Dog,Duck]
for a in animal_list:
    a().say()