fruit = ["Apple", "Banana","Mango"]
print(fruit)

"""
If you add new items to a list, 
the new items will be placed at the end of the list.
,
The list is changeable, meaning that we can change, add, 
and remove items in a list after it has been created.
"""



# I can Store Duplcate Value
duplicateList = ["Sakin", "Tamim", "Shawon", "Tamim"]
print(duplicateList)
print(len(duplicateList)) # 4

# Uses => Sob Rokom data store kora somvob
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

listMix = ["abc", 34, True, 40, "male"]
print(listMix[1]) # 34

# List declear via Constractor method
constructor = list(("Sakin","Tamim"))
print(type(constructor)) 