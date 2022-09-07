# L1
# message = 'hello world'
# print(message.upper())
# _______________________________________
# L2
# age = int(input('How old are you?'))
# if age >= 25:
#     print('You can come in alone')
# elif 18 <= age < 25:
#     print('You can come in with parents')
# else:
#     print('You cant come in')
# ________________________________________
# L3
# def hello():
#     print('Hello, World!')
#
#
# hello()
# hello()
# hello()
# x = int(input('Enter the first number:'))
# y = int(input('Enter the second number:'))
#
#
# def sum(a, b):
#     return a + b
#
#
# z = sum(x, y)
# print(z)
# a = 45
# b = 5
# print(a)
#
#
# def f():
#     global a
#     a = a + 2
#     print(a)
#
#
# f()
# __________________________________________________
# L4
# name = 'Hello, World!'
# for i in range(1, 11):
#     print(name)
# i = 1
# while i <= 10:
#     if i != 5:
#         print(i)
#     i += 1
#     continue
# _____________________________________________________
# L5
# nums = [2, 5, 8, 3, 4]
# # for num in nums:
# #     print(num)
# nums.append(56)
# print(nums)
# nums.pop()
# print(nums)
# ________________________________________________________
# L6
# tuple1 = ('first', 25, 25.1,)
# print(tuple1)
# print(tuple([45, 48, 145, 6]))
# print(list((45, 48, 145, 6)))
# dict1 = {'apple': 'red', 'banana': 'yellow', 'lemon': 'yellow'}
# print(dict1)
# for k in dict1.keys():
#     print(k)
# for k in dict1.values():
#     print(k)
# for k in dict1.items():
#     print(k)
# ______________________________________________________________
# L7
# print('Hello, World!')
# print('''Hello
# World
# !''')
# print('Hello\nHello\nHello')
# print('Hello\tHello\tHello')
# list1 = ['a', 'b', 'c']
# print(','.join(list1))
# str1 = '         Hello, World!            '
# print(str1.strip())
# ________________________________________________________________
# L8
# import math as m
#
# print(m.factorial(10))
# from math import factorial as f
# print(f(10))
# import ModuleExample as mex
# mex.hello()
# _________________________________________________________________
# L9
# f = open('1.txt', 'r')
# print(f.read())
# f.close()
# with open('1.txt', 'a') as f:
#     f.write(' My name is John!')
# try:
#     a = int(input())
#     b = int(input())
#     print(a / b)
# except ZeroDivisionError:
#     print('you can\'t divide by 0')
# ________________________________________________________________
# L10
# class House:
#     """house description"""
#
#     def __init__(self, street, number):
#         """house properties"""
#         self.street = street
#         self.number = number
#         self.age = 0
#
#     def build(self):
#         """build house"""
#         print('House at the street ' + self.street + ' with the number ' + str(self.number) + ' is built!')
#
#     def age_of_house(self, year):
#         """age of the house"""
#         self.age += year
#
#
# House1 = House('European', 9)
# House2 = House('European', 12)
# House1.build()
# House1.age_of_house(5)
# print(House1.age)
# class AvenueHouse(House):
#     """houses at the avenue"""
#
#     def __init__(self, ave, number):
#         self.ave = ave
#         super().__init__(self, number)
#
#
# AveHouse = AvenueHouse('Oleksanrovskyi', 25)
# print(AveHouse.ave)
# ________________________________________________________________________________________
# L11
# numbers = set([1, 1, 2, 4, 2])
# print(numbers)
# numbers = {1, 2, 3, 4, 5, 6, 7}
# for i in numbers:
#     print(i)
# numbers = {1, 2, 3, 4, 5, 6, 7}
# print(3 in numbers)
# numbers.add(58)
# numbers = {1, 2, 3, 4, 5, 6, 7}
# numbers1 = {2, 6, 54, 42, 3}
# numbers3 = numbers.union(numbers1)
# numbers3 = numbers | numbers1
# print(numbers3)
# _______________________________________________________________________________________
# L12
# import re
#
# s = 'ac/dcac/dcac/dcac/dcac/dcac/dcac/dcac/dcac/dcac/dcac/dcac/dc'
# result = re.match('ac', s)
# print(result)
# ______________________________________________________________________________________________
# L13
# import re
#
# s = 'Hello! How are you? I am fine.'
# result = re.findall(r'[bcdfghjklmnprstvwxzBCDFGHJKLMNPRSTVWXZ]\w+', s)
# print(result)
# _____________________________________________________________________________________
# L14
# print((lambda a, b: a if a > b else b)(15, 25))
# print((lambda a, b: a * b)(14, 16))
# ________________________________________________________________________________________
# L15
# with open('text54.txt') as f:
#     n = int(f.readline())
#     for i in range(n):
#         a, b = map(int, f.readline().split())
#         print(a, b)
#         print(a + b)
# def f(a, b):
#     return a * b
#
#
# # a = map(f, [2, 4, 5], [5, 6, 7])
# a = map(lambda x: x + 15, (2, 4, 5))
# print(list(a))
# def f(a):
#     if a % 2 == 0:
#         return a
#
#
# a = filter(f, (2, 4, 5))
# a = filter(lambda x: (x % 2 == 0), (2, 4, 5))
# print(list(a))
# from functools import reduce
#
# print(reduce(lambda a, b: a * b, (50, 57, 89, 12, 100)))
# a = [1, 2, 3, 4, 5, 6]
# b = 'abcdef'
# print(list(zip(a, b)))
# _________________________________________________________________________________
# L16
# def summ(*numbers):
#     print(sum(numbers))
#
#
# summ(1, 56, 74, 8, 9, 3)
# def brand(**brands):
#    for x, y in brands.items():
#        print(x, ':', y)
#
#
# brand(a='apple', b='samsung')
# -----------------------------------------------------------------------------
# L17
# s = []
# for i in range(1, 21):
#     if i % 5 == 0:
#         s.append(i)
# print(s)
# # generator
# s1 = [i ** 3 for i in range(1, 21) if i % 5 == 0]
# print(s1)
# s = []
# for i in range(1, 21):
#     for j in range(1, 51):
#         s.append((i, j))
# print(s)
#
# s1 = [(i, j) for i in range(1, 21) for j in range(1, 51)]
# print(s1)
# s = []
# for i in range(-10, 11):
#     if i > 0:
#         s.append(i ** 2)
#     else:
#         s.append(i ** 3)
# print(s)
# s1 = [i ** 2
#       if i > 0
#       else i ** 3
#       for i in range(-10, 11)
#       if i % 2 == 0]
# print(s1)
# s = [7, 8, 8, -10, -10]
# set_set = {i for i in s}
# print(set_set)
# dictionary = {i: i ** 10 for i in s}
# print(dictionary)
# ---------------------------------------------------------------------------
# # L18
# import builtins
# print(dir(builtins))
# y = 2
#
#
# def degree(x):
#     return y ** x
#
#
# print(degree(4))
# def degree(x):
#     y = 2
#     return y ** x
#
#
# print(degree(4))
# def degree(x):
#     y = 2
#
#     def degree_two():
#         return y ** x
#
#     return degree_two()
#
#
# print(degree(4))
# def message(number):
#     def print_message():
#         return 'Number ' + str(number)
#
#     return print_message()
#
#
# print(message(78))
# def message(x):
#     def print_message(y):
#         return x, y
#
#     return print_message
#
#
# d = message(4)
# print(d(8))
# print(d(5))
# print(d(6))
# ------------------------------------------------------------------
# L19
# def decor(func):
#     def wrapper(n):
#         print('start')
#         func(n)
#         print('end')
#
#     return wrapper
#
#
# @decor
# def my_func(number):
#     print(number ** 2)
#
#
# my_func(10)
# import time
#
#
# def my_decor(func):
#     def my_wr():
#         start_time = time.time()
#         func()
#         print(time.time() - start_time)
#
#     return my_wr
#
#
# @my_decor
# def sp():
#     list1 = [i ** 2 for i in range(100000) if i % 2 == 0]
#     print(list1)
#
#
# sp()
