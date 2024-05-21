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

def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

print(create_cubes(10))

for x in create_cubes(10):
    print(x)