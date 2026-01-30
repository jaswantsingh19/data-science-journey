# Loops in Python
# Loops are used to repeat instructions.
# while Loops
# while condition :
# #some work
# print hello 5 times
# print numbers from 1 to 5
# show infinite, iterator


# Break & Continue
# Break : used to terminate the loop when encountered.
# Continue : terminates execution in the current iteration &
# continues execution of the loop
# with the next iteration.
# take search example
# & stop the search when found
# print all numbers but not multiple of 3


# for Loops
# Loops are used used for sequential traversal.
# For traversing list, string, tuples etc.
#
# for element in list:
# for = Reserved keyword
# element = variable given to all the values in the list
# For Example:
# list = [1, 2, 3]
# for element in list:
# for any_variable_value in list:
#     print(any_variable_value)

# for Loop with else

# list = [1, 2, 3]
# # For Example:
# # for element in list:
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
