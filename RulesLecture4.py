# Dictionary in Python
# Dictionaries are used to store data values in "key:value" pairs
# They are unordered, mutable(changeable) & don’t allow duplicate keys
# For example:
dict = {
    "name": "Jaswant Singh",  # Key: name, Value: Jaswant Singh
    "age": 36,  # Key: age, Value: 36
    "city": "Chandigarh",  # Key: city, Value: Chandigarh
    "marks": [98, 97, 95],  # Key: marks, Value: [98, 97, 95]
    "isGraduated": True,  # Key: isGraduated, Value: True
}

# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries
# For example:
nested_dict = {
    "name": "Jaswant Singh",  # Key: name, Value: Jaswant Singh
    "age": 36,  # Key: age, Value: 36
    "city": "Chandigarh",  # Key: city, Value: Chandigarh
    "education": {  # Nested Dictionary with key education
        "undergraduate": "B.Tech",  # Key: undergraduate, Value: B.Tech
        "postgraduate": "M.Tech",
    },  # Key: postgraduate, Value: M.Tech
}

# Dictionary Methods
# myDict.keys( )  #returns all keys
# For example:
myDict = {
    "name": "Jaswant Singh",
    "age": 36,
    "city": "Chandigarh",
}
# myDict.keys( )  #returns all keys
# Output: dict_keys(['name', 'age', 'city'])


# myDict.values( )  #returns all values
# Output: dict_values(['Jaswant Singh', 36, 'Chandigarh'])

# myDict.items( )  #returns all (key, val) pairs as tuples
# Output: dict_items([('name', 'Jaswant Singh'), ('age', 36), ('city', 'Chandigarh')])

# myDict.get( "key" )  #returns the key according to value
# myDict.get( "name" )  # Output: 'Jaswant Singh'

# myDict.pop( "key" )  # removes the item with the specified key name
# myDict.pop( "age" )  # Output: removes the item with key 'age'

# myDict.popitem( )  # removes the last inserted item
# myDict.popitem( )  # Output: removes the last inserted item

# myDict.clear( )  #removes all the items from the dictionary
# myDict.clear( )  # Output: {}

# myDict.copy( )  #returns a copy of the dictionary
# newDict = myDict.copy( )  #creates a copy of myDict

# myDict.update( newDict )  #inserts the specified items to the dictionary
# newDict = {"country": "India"}
# myDict.update( newDict )  #adds the key:value pair from newDict to myDict
# Output: {'name': 'Jaswant Singh', 'age': 36, 'city': 'Chandigarh', 'country': 'India'}


# Set in Python
# Set is the collection of the unordered items.
# Each element in the set must be unique & immutable.
# Sets are mutable, meaning we can add or remove items from it.

# For example:
# mySet = {"apple", "banana", "cherry"}
# Note: Sets are unordered, so the items will appear in a random order
# Output: {'banana', 'cherry', 'apple'}

# For example:
# nums = {1, 2, 3, 4}
# set2 = {1, 2, 2, 2}
# repeated elements stored only once, so it resolved to {1, 2}
# print(set2) # output: {1, 2}
# print(nums) # output: {1, 2, 3, 4}

# null_set = set()
# empty set syntax
# print(type(null_set)) # output: <class 'set'>

# Set Methods
# set.add( el )  #adds an element
# set.add( "orange" )  #adds "orange" to the set

# set.remove( el )  #removes the elem an
# set.remove( "banana" )  #removes "banana" from the set

# set.clear( )  #empties the set
# set.clear( )  # Output: set()

# set.pop( )  #removes a random value
# set.pop( )  # Output: removes a random value from the set

# set.union( set2 )  #combines both set values & returns new
# For example:
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# set1.union( set2 )  # Output: {1, 2, 3, 4, 5}

# set.intersection( set2 )  #combines common values & returns new
# For example:
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# set1.intersection( set2 )  # Output: {3}

# set.difference( set2 )  #returns values in set1 not in set2
# For example:
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# set1.difference( set2 )  # Output: {1, 2}

# set.symmetric_difference( set2 )  #returns values in either set1 or set2 but not in both
# For example:
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# set1.symmetric_difference( set2 )  # Output: {1, 2, 4, 5}
