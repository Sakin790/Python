"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dictionary
Set Types:	set, frozenset
Boolean Type:	True / False
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

# int/PurnoShongha
x= 10
print(type(x))  #<class 'int'>

# String
name= "Mahid"
print(type(name)) #<class 'str'>

#Float
floatNumber= 20.5
print(type(floatNumber)) # <class 'float'>

# Complex number
complexNumber = 5+6j
sum = complexNumber * 2
print(sum) # (10+12j)

#List
list = ["apple", "banana", "cherry"] 
"""
List:
1.Lists are a built-in data structure in Python.
2.They can hold elements of different data types.
3.Lists are dynamic and resizable, meaning you can add, remove, or modify elements freely.
4.Lists support a variety of methods for manipulation such as append(), remove(), pop(), etc.
5.Lists are part of the standard Python library (list type) and are widely used for general-purpose data storage and manipulation.
"""

# Tuple
x = ("apple", "banana", "cherry")
# We will learn more in future
print(x[1]) # via index

# Set
x = {"apple", "banana", "cherry"} # 2nd Bracket

#Dictionary
x = {"name" : "John", "age" : 36} # key value pair like object o

#frozenset 
tuple + set
x = frozenset({"apple", "banana", "cherry"})