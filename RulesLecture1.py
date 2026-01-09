# Data Types
# Integers
# String
# Float
# Boolean
# None


# Comments in Python
# # Single Line Comment
# """
# Multi Line
# Comment
# """


# Types of Operators
# An operator is a symbol that performs a certain operation between operands.
# Arithmetic Operators ( + , - , * , / , % , ** )
# Relational / Comparison Operators ( == , != , > , < , >= , <= )
# Assignment Operators ( = , +=, -= , *= , /= , %= , **=  )
# Apna College
# Logical Operators ( not , and , or )


# Function
# Description
# int(y [base])
# It converts yto an integer, and Base specifies the number base. For example, if
# you want to convert the string in decimal numbers then you'll use 10 as base.
# float(y)
# It converts yto a floating-point number.
# complex(real
# It creates a complex number.
# Apna
# [imag])
# str(y)
# It converts yto a string.
# tuple(y)
# It converts yto a tuple.
# list(y)
# It converts yto a list.
# set(y)
# It converts yto a set.
# dict(y)
# It creates a dictionary and y should be a sequence of (key, value) tuples.
# ord(y)
# It converts a character into an integer.
# hex(y)
# It converts an integer to a hexadecimal string.
# oct(y)
# It converts an integer to an octal string


# Input in Python
# input( ) statement is used to accept values (using keyboard) from user
# input( )  #result for input( ) is always a str
# int ( input( ) )  #int
# float ( input( ) )   #float


# name = "Jaswant Singh"
# age = 36
# height = 5.8
# married = False
# print("Name:", name, type(name))  # Name: Jaswant Singh <class 'str'>
# print("Age:", age, type(age))  # Age: 36 <class 'int'>
# print("Height:", height, type(height))  # Height: 5.8 <class 'float'>
# print("Married:", married, type(married))  # Married: False <class 'bool'>
# # This is a simple Python program that defines variables of different
# # data types and prints their types and values.


# # Arithmetic Operations
# a = 79
# b = 21
# print("Addition:", a + b)  # Addition: 100
# print("Subtraction:", a - b)  # Subtraction: 58
# print("Multiplication:", a * b)  # Multiplication: 1659
# print("Division:", a / b)  # Division: 3.761904761904762
# print("Floor Division:", a // b)  # Floor Division: 3
# print("Modulus:", a % b)  # Modulus: 16
# print("Exponentiation:", a**b)  # Exponentiation: 5585458640832840079389441
# # This program performs various arithmetic operations on two numbers
# # and prints the results.


# # Relational Operators
# a = 10
# b = 5
# print(a == b)  # False
# print(a != b)  # True
# print(a > b)  # True
# print(a < b)  # False
# print(a >= b)  # True
# print(a <= b)  # False
# # This program compares two numbers using relational operators
# # and prints the boolean results.


# # Assignment Operators
# a = 10
# b = 5
# a += b
# print("a += b:", a)  # a += b: 15
# a -= b
# print("a -= b:", a)  # a -= b: 10
# a *= b
# print("a *= b:", a)  # a *= b: 50
# a /= b
# print("a /= b:", a)  # a /= b: 10.0
# a %= b
# print("a %= b:", a)  # a %= b: 0.0
# # This program demonstrates the use of assignment operators
# # by performing operations on a variable and printing the results.


# # Logical Operators
# a = True
# b = False
# print("a and b:", a and b)  # a and b: False
# print("a or b:", a or b)  # a or b: True
# print("not a:", not a)  # not a: False
# print("not b:", not b)  # not b: True
# # This program uses logical operators to evaluate boolean expressions
# # and prints the results.


# # Type Casting
# # Implicit Type Casting
# a = 5  # int
# b = 2.0  # float
# c = a + b  # int + float = float
# print(
#     "Implicit Type Casting:", c, type(c)
# )  # Implicit Type Casting: 7.0 <class 'float'>
# # Explicit Type Casting
# x = 10  # int
# y = float(x)  # int to float
# z = str(x)  # int to str
# print(
#     "Explicit Type Casting to float:", y, type(y)
# )  # Explicit Type Casting to float: 10.0 <class 'float'>
# print(
#     "Explicit Type Casting to str:", z, type(z)
# )  # Explicit Type Casting to str: 10 <class 'str'>
# # This program demonstrates both implicit and explicit type casting
# # and prints the results along with their types.
# # The program covers basic data types, arithmetic operations,
# # relational operators, assignment operators, logical operators,
# # and type casting in Python.
