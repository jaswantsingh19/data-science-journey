# Lists in Python
# A built-in data type that stores set of values
# It can store elements of different types (integer, float, string, etc.)
# Lists are mutable, meaning their elements can be changed after creation
# Lists are ordered, meaning the elements have a defined order and that
# they can be accessed by their index

# marks = [87, 64, 33, 95, 76]  ## marks[0], marks[1]..
# marks[2] = 40  ## allowed in lists
# marks is now [87, 64, 40, 95, 76]
# len(marks)  ## returns length of list

# student = ["Karan", 85, "Delhi"]  ## student[0], student[1]..
# student[0] = "Arjun"  ## allowed in lists
# student is now ["Arjun", 85, "Delhi"]
# len(student)  ## returns length of list

# List Slicing
# Similar to String Slicing
# list_name[ starting_idx : ending_idx ] ## ending idx is not included
# marks = [87, 64, 33, 95, 76]
# marks[ 1 : 4 ] is [64, 33, 95]
# marks[  : 4 ] is same as marks[ 0 : 4] and is [87, 64, 33, 95]
# marks[ 1 :  ] is same as marks[ 1 : len(marks) ] and is [64, 33, 95, 76]
# marks[ : ] is same as marks[ 0 : len(marks) ] and is [87, 64, 33, 95, 76]
# marks[ -4 : -1 ] is [64, 33, 95]
# marks[ -3 : -1 ] is [33, 95]
# marks[ -3 :  ] is [33, 95, 76]
# marks[ : -1 ] is [87, 64, 33, 95]
# Negative indexing starts from the end of the list


# List Methods
# list = [2, 1, 3]
# list.append(4)  # adds one element at the end # results [2, 1, 3, 4]
# list.sort( )  #sorts in ascending order # results [1, 2, 3]
# list.sort( reverse=True )  #sorts in descending order # results [3, 2, 1]
# list.reverse( )  #reverses list # results [3, 1, 2]

# list.insert( idx, el )  # insert element at index idx
# For Example:
# results: list.insert(1, 4) # results [2, 4, 1, 3]

# list.extend( another_list )  #adds all elements of another_list at the end
# For Example:
# results: list.extend( [4, 5] ) # results [2, 1, 3, 4, 5]

# list.count( el )  #counts total occurrences of el in list
# results: list.count(1) is 1
# list.index( el )  #returns index of first occurrence of el
# results: list.index(3) is 2


# List Methods
# list = [2, 1, 3, 1]
# list.remove(1)  #removes first occurrence of element # results [2, 3, 1]

# list.pop( idx )  #removes element at idx and returns it
# For Example:
# results: list.pop(1) is 1, list is now [2, 3, 1]

# list.pop( )  #removes last element and returns it
# For Example:
# results: list.pop() is 1, list is now [2, 1, 3]

# list.clear( )  #removes all elements from list # results []


# Tuples in Python
# A built-in data type that lets us create immutable sequences of values.
# Tuples are similar to lists, but unlike lists,
# tuples cannot be changed after creation.
# Tuples are defined using parentheses ( ) instead of square brackets [ ].
# Tuples are ordered, meaning the elements have a defined order and
# can be accessed by their index.

# Examples:
# tup = (87, 64, 33, 95, 76) #tup[0], tup[1]..
# tup[0] = 43 #NOT allowed in tuples
# tup is still (87, 64, 33, 95, 76)
# tup1 = ( ) #empty tuple
# tup2 = ( 1, ) #single element tuple
# tup3 = ( 1, 2, 3 ) #multiple element tuple
# len(tup) #returns length of tuple

# Tuple Slicing
# Similar to String & List Slicing
# tup = (87, 64, 33, 95, 76)
# tup[ 1 : 4 ] is (64, 33, 95)
# tup[  : 4 ] is same as tup[ 0 : 4] and is (87, 64, 33, 95)
# tup[ 1 :  ] is same as tup[ 1 : len(tup) ] and is (64, 33, 95, 76)
# tup[ : ] is same as tup[ 0 : len(tup) ] and is (87, 64, 33, 95, 76)
# tup[ -4 : -1 ] is (64, 33, 95)
# tup[ -3 : -1 ] is (33, 95)
# tup[ -3 :  ] is (33, 95, 76)
# tup[ : -1 ] is (87, 64, 33, 95)
# Negative indexing starts from the end of the tuple


# Tuple Methods
# tup = (2, 1, 3, 1)
# tup.index( el )  #returns index of first occurrence of el
# tup.index(1) is 1 #first occurrence of 1 is at index 1

# tup.count( el )  #counts total occurrences of el in tuple
# tup.count(1) is 2 #1 occurs twice in the tuple
# Example:
# tup = (2, 1, 3, 1)
# tup.index(1) is 1
# tup.count(1) is 2
# Note: Tuples have only two methods - index( ) and count( )
# because they are immutable.
