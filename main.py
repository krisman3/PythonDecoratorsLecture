# def func():
#     return 1
#
#
# def hello(name="Jose"):
#     print("The hello function has been executed!")
#
#     def greet():
#         return '\t This is the greet() function inside hello!'
#
#     def welcome():
#         return '\t This is welcome() inside hello'
#
#     print("I am going to return a function!!")
#
#     if name == "Jose":
#         return greet
#     else:
#         return welcome
#
# my_new_func = hello("Jose")
# print(my_new_func())

# def cool():
#
#     def super_cool():
#         return "I am very cool!"
#
#     return super_cool()
#
# some_func = cool()
#
# some_func()

# def hello():
#     return "Hi Jose!"
#
# def other(some_def_func):
#     print("Other code runs here!")
#     print(some_def_func())
#
# other(hello)

# def new_decorator(original_function):
#
#     def wrap_func():
#         print("Some extra code, before the original functions")
#
#         original_function()
#
#         print("Some extra code, after the original function")
#
#     return wrap_func
#
# # def func_needs_decorator():
# #     print("I want to be decorated!!")
# #
# # # func_needs_decorator()
# #
# # decorated_func = new_decorator(func_needs_decorator)
# #
# # decorated_func()
#
# @new_decorator
# def func_needs_decorator():
#     print("I want to be decorated!!")
#
# func_needs_decorator()

# def create_cubes(n):
#
#    for x in range(n):
#        yield x**3
#
# print(create_cubes(10))
#
# for x in create_cubes(10):
#     print(x)

# def gen_fibon(n):
#     a = 1
#     b = 1
#     for i in range(n):
#         yield a
#         a, b = b, a+b
#
# for number in gen_fibon(10):
#     print(number)

# def simple_gen():
#     for x in range(3):
#         yield x
#
#
# # for number in simple_gen():
# #     print(number)
#
# g = simple_gen()
#
# s = 'Hello'
#
# for letter in s:
#     print(letter)
#
# s_iter = iter(s)
# print(next(s_iter))


"""
Iterators and Generators Homework
Problem 1
Create a generator that generates the squares of numbers up to some number N.
"""


def gensquares(n):
    for x in range(n):
        yield x**2


for number in gensquares(10):
    print(number)


"""
Problem 2
Create a generator that yields "n" random numbers between a low and high number (that are inputs).
"""


import random


def rand_num(low, high, n):
    for x in range(n):
        yield random.randint(low, high)


for number in rand_num(1, 10, 5):
    print(number)
