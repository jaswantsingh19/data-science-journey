# Strings
# String is data type that stores a sequence of characters.


# Basic Operations

# concatenation
# “hello” + “world” resulets in “helloworld”

# repetition
# “hello” * 3 results in “hellohellohello”

# length of str
# len(str)


# Indexing
# str = “Apna_College”
# str[0] is ‘A’, str[1] is ‘p’ ...
# str[0] = ‘B’ #not allowed


# Slicing
# Accessing parts of a string
# str[ starting_idx : ending_idx ] #ending idx is not included
# str = “ApnaCollege”
# str[ 1 : 4 ] is “pna”
# str[  : 4 ] is same as str[ 0 : 4]
# str[ 1 :  ] is same as str[ 1 : len(str) ]

# Slicing
# Negative Index
# A  p  p  l  e
# -5 -4 -3 -2 -1
# str = “Apple”
# str[ -3 : -1 ] is “pl”


# String Functions
# str = “I am a coder.”
# str.endsWith(“er.“)  #returns true if string ends with substr
# str.capitalize( )  #capitalizes 1st char
# str.replace( old, new )  #replaces all occurrences of old with new
# str.find( word )  #returns 1st index of 1st occurrence of substr
# str.lower( )  #converts string to lowercase
# str.upper( )  #converts string to uppercase
# str.strip( )  #removes leading & trailing whitespaces
# str.count(“am“)  #counts the occurrence of substr in string


# Conditional Statements
# if-elif-else (SYNTAX)

# if(condition) :
#     Statement1
# elif(condition):
#     Statement2
# else:
#     StatementN
# # Indentation is important in Python to define code blocks.


# Conditional Statements
# Grade students based on marks
# marks >= 90, grade = “A”
# 90 > marks >= 80, grade = “B”
# 80 > marks >= 70, grade = “C”
# 70 > marks, grade = “D”
