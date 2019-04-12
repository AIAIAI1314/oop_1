#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test2.py
# @Author: Hu


'''class Teacher():

    name = "hello"
    age = 19

    def say(self):
        self.name="world"
        self.age=20
        print("my name is {}".format(self.name))
        print("my age is {}".format(self.age))
# 访问类的成员时用 __class__成员名
    def sayagain():
        print( __class__.name )
        print( __class__.age )
        print("Hello to see you again")'''

# t1 = Teacher()
################
# 调用绑定类的类函数使用类名#
# Teacher.sayagain()

# t1.say()


''' class A():
    name = "A"
    age = 90

    # 构造函数

    def __init__(self):
        self.name = "B"
        self.age = 12
        # self.time = 13

    def say(self):
        print(self.name)
        print(self.age)
        # print(self.time)


class C():
    name = "C"
    age = 18
    time = 0
a=A()
# 默认将a作为参数传入
a.say()
# 此时self被a替换
A.say(a)
# 同样可以把A作为参数传入
A.say(A)
# 将B作为参数传入，只要类中有同样的成员
A.say(C) '''


class Person():
    name = "li"
    __age = 18
print("Person的名字是{}".format(Person.name))
# print("Person的年龄是{}".format(Person.age)) #无法访问





