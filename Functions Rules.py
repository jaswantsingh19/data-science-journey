# Functions in Python
# Block of statements that perform a specific task.

# def func_name( param1, param2..) :
# return val
# func_name( arg1, arg2 ..) #function call

# For Example:
# def sum(a, b):
#     s = a + b
#     return s


# print(sum(2, 3))


# For Example:
# def sum(a, b):
#     s = a + b
#     print(s)


# sum(2, 3)


# For Example:
# def cal_sum(a, b):
#     return a + b


# print(cal_sum(1, 3))


# For Example:
# def cal_sum(a, b):
#     return a + b


# val = cal_sum(1, 3)
# print(val)


# For Example:
# def a():
#     print("Hello!!!", "Hola")


# a()
# a()
# a()


# For Example:
# def a():
#     print("Hello!!!", "Hola")


# output = a()
# results: "Hello!!! Hola"

# print(output)  # None
# because function has no return statement
# when we try to print a variable which stores function call result
# it shows None as output


# For Example:
# Average of 3 numbers with functions
# def avg(a, b, c):
#     return (a + b + c) / 3


# print(avg(4, 6, 6))


# def cal_avg(a, b, c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return avg


# cal_avg(4, 6, 6)


# Functions in Python
# Built-in Functions & User defined Functions.
# Built-in Functions
# print( )
# len( )
# type( )
# range( )


# Default Parameters
# Assigning a default value to parameter,
# which is used when no argument is passed.
# def cal_avg(a=1, b=1, c=1):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return avg


# cal_avg()


# Recursion
# When a function calls itself repeatedly.
# #prints n to 1 backwards
# def show(n):
#     if n == 0:  # Base case
#         return
#     print(n)
#     show(n - 1)


# Recursion
# #returns n!
# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)


print(r"Python is \"awesome\"")

