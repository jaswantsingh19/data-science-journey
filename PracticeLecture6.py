# Let‘s Practice
# WAF to print the length of a list. ( list is the parameter)
# def a(list):
#     print(len(list))


# i = [1, 4, 7, 9, 0, 2, 1]
# a(i)


# WAF to print the elements of a list in a single line. ( list is the parameter)
# def a(list):
#     for b in list:
#         print(b, end=" ")


# i = [1, 4, 7, 9, 0, 2, 1]
# a(i)


# WAF to find the factorial of n. (n is the parameter)
# def a(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#         print(fact, i)


# a(5)


# WAF to convert USD to INR.
# def usd(n):
#     inr = n * 83
#     print(inr)
#     return inr


# usd(7)


# def a(usd_val):
#     inr = usd_val * 83
#     print(usd_val, "USD =", inr, "INR")


# a(7)


# def a(n):
#     if n % 2 == 0:
#         print("Entered Number is Even")
#     else:
#         print("Entered Number is Odd")


# a(int(input("Enter a Number : ")))


# Let‘s Practice
# Write a recursive function to calculate the sum of first n natural numbers.
# def recursive_sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n + recursive_sum(n - 1)


# print(recursive_sum(5))


# def a(n):
#     if n == 1:
#         return 1
#     else:
#         return n + a(n - 1)


# print(a(5))


# def a(n):
#     if n == 0:
#         return 0
#     return a(n - 1) + n


# sum = a(5)
# print(sum)


# Write a recursive function to print all elements in a list.
# Hint : use list & index as parameters.
# def print_list(list, index=0):
#     if index == len(list):
#         return
#     print(list[index])
#     print_list(list, index + 1)


# my_list = ["apple", "banana", "cherry", "date"]
# print_list(my_list)
