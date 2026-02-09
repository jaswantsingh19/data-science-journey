# Loops in Python
# Loops are used to repeat instructions.
# Two types of loops in Python: While Loops & For Loops

# while Loops
# Repeats a block of code as long as a specified condition is true.
# Syntax:
# while condition:
#     # code block to be executed
# Example:
# count = 1
# while count <= 5:
#     print("hello")
#     count += 1  # incrementing count to avoid infinite loop
# Output:
# hello
# hello
# hello
# hello
# hello


# Infinite Loops
# A loop that never ends.
# Example:
# while True:
#     print("infinite loop")

# iterator
# An object that contains a countable number of values.
# An iterator is an object that can be iterated upon,
# meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements
# the iterator protocol, which consists of the methods __iter__() and __next__().
# Example:
# myList = [1, 2, 3]
# myIter = iter(myList)  # creating an iterator object
# print(next(myIter))  # Output: 1

# Another Example:
# count = 1
# while count <= 5: # iterator here is count
#     print("hello")
#     count += 1  # incrementing count to avoid infinite loop
# Output:
# hello
# hello
# hello
# hello
# hello

# Another Example:
# a = 0
# while a < 3:  # iterator here is a
#     print(a)
#     a += 1
# Output:
# 0
# 1
# 2

# Break & Continue
#
# Continue : terminates execution in the current iteration &
# continues execution of the loop with the next iteration.
# take search example & stop the search when found
# print all numbers but not multiple of 3
# Example of Continue:
# count = 1
# while count <= 10:
#     if count % 3 == 0:
#         count += 1
#         continue
#     print(count)
#     count += 1
# Output:
# 1
# 2
# 4
# 5
# 7
# 8

#  Break : used to terminate the loop when encountered.
# It exits the loop completely.
# take search example & stop the search when found.
# Example of Break:
# count = 1
# while count <= 10:
#     if count == 6:
#         break # exit loop when count is 6
#     print(count)
#     count += 1
# Output:
# 1
# 2
# 3
# 4
# 5


# for Loops
# Loops are used used for sequential traversal.
# For traversing list, string, tuples etc.
#
# for element in list:
# for = Reserved keyword
# element = variable given to all the values in the list
# For Example:
# list = [1, 2, 3]
# for any_variable_value in list:  # any_variable_value takes values 1, 2, 3 one by one
#     print(any_variable_value)

# for Loop with else
# list = [1, 2, 3]
# # For Example:
# for any_variable_value in list:
#     print(any_variable_value)
# else:
#     print("END")
# # work when loop ends

# # else used as it doesn’t execute
# # when break is used
# # For Example:
# name = "Jaswant"
# for letters in name:
#     if letters == "w":
#         print("w found")
#         break
#     print(letters)
# print("End")


# for loop with strings
# For Example:
# name = "Jaswant"
# for letters in name:
#     print(letters)
# Output
# J
# a
# s
# w
# a
# n
# t


# Using range( ) in for loop
# Range functions returns a sequence of numbers,
# starting from 0 by default, and increments by 1 (by default),
# and stops before a specified number.
# range( start?, stop, step?)
# For Example:
# for el in range(5):
#     print(el)

# for el in range(1, 5):
#     print(el)

# for el in range(1, 100, 2): #prints odd numbers
#     print(el)

# for el in range(2, 100, 2): #prints even numbers
#     print(el)


# pass Statement
# pass is a null statement that does nothing.
# It is used as a placeholder for future code.
# for el in range(10):
# pass
# generally used in execption handling
