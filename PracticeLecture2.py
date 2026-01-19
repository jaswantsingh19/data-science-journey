# # Let‘s Practice
# # WAP to input user’s first name & print its length.
# first_name = input("Enter your first name: ")
# print("Length of your first name is:", len(first_name))


# # WAP to find the occurrence of ‘$’ in a String.
# dollars = input("Enter an amount with currency symbol: ")
# count_dollars = dollars.count("$")
# print("Number of occurrences of '$':", count_dollars)


# # WAP to check if a number entered by the user is odd or even.
# a = int(input("Guess any number: "))
# if a % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")


# WAP to find the greatest of 3 numbers entered by the user.
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# if (num1 >= num2) and (num1 >= num3):
#     print("The Greatest Number is the first number:", num1)
# elif (num2 >= num3) and (num2 >= num1):
#     print("The Greatest Number is the second number:", num2)
# else:
#     print("The Greatest Number is the third number:", num3)


# # WAP to check if a number is a multiple of 7 or not.
# num = int(input("Enter a number: "))
# if num % 7 == 0:
#     print(num, "is a multiple of 7.")
# else:
#     print(num, "is not a multiple of 7.")


# # WAP to check if a year entered by the user is a leap year or not.
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(year, "is a leap year.")
# else:
#     print(year, "is not a leap year.")
# (A year is a leap year if it is divisible by 4 but not by 100,
# except if it is divisible by 400.)


# # WAP to input a character & check if it is a vowel or consonant.
# letter = input("Enter a letter of the alphabet: ").lower()
# if letter in "aeiou":
#     print(letter, "is a vowel.")
# else:
#     print(letter, "is a consonant.")


# # WAP to input a character & check if it is an alphabet, digit or special character.
# character = input("Enter a character: ")
# if character.isalpha():
#     print(character, "is an alphabet.")
# elif character.isdigit():
#     print(character, "is a digit.")
# else:
#     print(character, "is a special character.")


# # WAP to input 3 sides of a triangle & check if it is
# # equilateral, isosceles or scalene triangle.
# side1 = float(input("Enter Length of the first side of the triangle: "))
# side2 = float(input("Enter Length of the second side of the triangle: "))
# side3 = float(input("Enter Length of the third side of the triangle: "))
# if side1 == side2 == side3:
#     print("The triangle is Equilateral.")
# elif side2 == side3 or side1 == side3 or side1 == side2:
#     print("The triangle is Isosceles.")
# else:
#     print("The triangle is Scalene.")


# # WAP to input marks of 5 subjects & print the division obtained.
# English = float(input("Enter marks obtained in english: "))
# Maths = float(input("Enter marks obtained in maths: "))
# Science = float(input("Enter marks obtained in science: "))
# Hindi = float(input("Enter marks obtained in hindi: "))
# Social_Science = float(input("Enter marks obtained in social science: "))
# total_marks_obtained = English + Maths + Science + Hindi + Social_Science
# percentage = (total_marks_obtained / 500) * 100
# if percentage >= 60:
#     print("First Division")
# elif percentage >= 45:
#     print("Second Division")
# elif percentage >= 33:
#     print("Third Division")
# else:
#     print("Fail")
# # (First Division: 60% & above, Second Division: 45% to 59%,
# # Third Division: 33% to 44%, Fail: below 33%)


# WAP to input a month number (1-12) & print the number of days in that month.
# WAP to input temperature in Celsius & convert it to Fahrenheit.
# WAP to input a character & check if it is uppercase or lowercase.
# WAP to input a string & check if it is a palindrome or not.
# WAP to input a year & check if it is a century year or not.
# (A century year is divisible by 100.)
# WAP to input a number & check if it is positive, negative or zero.
# WAP to input a character & check if it is a digit or not.
# WAP to input a number & check if it is a three-digit number or not.
# WAP to input a number & check if it is divisible by both 3 and 5.
# WAP to input a character & check if it is a whitespace character or not.
# WAP to input a number & check if it is a prime number or not.
# WAP to input a string & check if it contains only alphabets.
# WAP to input a number & check if it is a perfect square or not.
# WAP to input a number & check if it is a perfect cube or not.
# WAP to input a number & check if it is an Armstrong number or not.
# (An Armstrong number is equal to the sum of its own digits each
# raised to the power of the number of digits.)
# WAP to input a character & check if it is a punctuation mark or not.
# WAP to input a number & check if it is a power of 2 or not.
# WAP to input a string & check if it contains any digits.
# WAP to input a number & check if it is a palindrome or not.
# WAP to input a number & check if it is even or odd using bitwise operators.
# WAP to input a character & check if it is a vowel or consonant using a set.
# WAP to input a number & check if it is divisible by 3 or 5.
# WAP to input a number & check if it is a multiple of 10 or not.
# WAP to input a number & check if it is a two-digit number or not.
# WAP to input a number & check if it is a four-digit number or not.
