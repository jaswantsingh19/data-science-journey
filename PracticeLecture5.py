# Loops in Python
# Loops are used to repeat instructions.
# Types of loops: While Loops and For Loops
#
#
# Let‘s Practice While Loops
# Print numbers from 1 to 100.
# a = 1
# while a <= 100:
#     print(a)
#     a += 1

# Print numbers from 100 to 1.
# a = 100
# while a >= 1:
#     print(a)
#     a -= 1


# Print the multiplication table of a number n.
# n = int(input("Table Number : "))
# a = 1
# while a <= 10:
#     print(a * n)
#     a += 1

# Print the elements of the following list using a loop:
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# n = 0
# while n <= len(a) - 1:
#     print(a[n])
#     n += 1


# Search for a number x in this tuple using loop:
# a = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = int(input("Enter a number: "))
# b = 0
# while b <= len(a) - 1:
#     if (a[b]) == x:
#         print("Found at index:", b)
#     else:
#         print("finding")
#     b += 1


# Break & Continue
# Break : used to terminate the loop when encountered.
# a = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = int(input("Enter a number: "))
# b = 0
# while b <= len(a) - 1:
#     if (a[b]) == x:
#         print("Found at index:", b)
#         break
#     else:
#         print("finding")
#     b += 1


# Continue : terminates execution in the current iteration &
# continues execution of the loop
# with the next iteration.
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# x = int(input("Enter a number: "))
# n = 0
# while n <= len(a) - 1:
#     if n == x:
#         n += 1
#         continue
#     print(a[n])
#     n += 1

# Even/Odd Numbers using Continue in While Loops
# n = 1
# while n <= 100:
#     if n % 2 != 0:
#         n += 1
#         continue
#     print(n)
#     n += 1


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


# Let‘s Practice
# using for

# Print the elements of the following list using a loop:
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for b in a:
#     print(b)

# Search for a number x in this tuple using loop:
# a = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = int(input("enter a num: "))
# ind = 0
# for b in a:
#     print(b)
#     if b == x:
#         print("Found number:", x, "at index:", ind)
#         break
#     ind += 1
# print("END")


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


# Let‘s Practice
# using for & range( )

# Print numbers from 1 to 100.
# for a in range(1, 101):
#     print(a)

# Print numbers from 100 to 1.
# for a in range(100, 0, -1):
#     print(a)

# Print the multiplication table of a number n.
# x = int(input("Enter any number: "))
# for a in range(1, 11):
#     print(x * a)


# pass Statement
# pass is a null statement that does nothing.
# It is used as a placeholder for future code.
# for el in range(10):
# pass
# generally used in execption handling


# Let‘s Practice
# WAP to find the sum of first n numbers.
# (using for and while both seperatly)
# n = int(input("Enter any number: "))
# sum = 0
# for a in range(1, n + 1):
#     sum += a
#     print(a)
# print("Sum of numbers from 1 till", n, "is :", sum)

# n = int(input("Enter any number: "))
# sum = 0
# i = 0
# while i < n:
#     sum += i
#     i += 1
#     print(i)
# print("Sum of numbers from 1 till", n, "is :", sum)

# WAP to find the factorial of first n numbers.
# (using for and while both seperatly)
# n = int(input("Enter any number: "))
# factorial = 1
# for a in range(1, n + 1):
#     factorial *= a
#     print(a)
# print("Factorial of numbers from 1 till", n, "is :", factorial)

# n = int(input("Enter any number: "))
# factorial = 1
# a = 0
# while a < n:
#     a += 1
#     factorial *= a
#     print(a)
# print("Factorial of numbers from 1 till", n, "is :", factorial)
