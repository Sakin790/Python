age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

"""
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
"""

# Via Index
quantity = 3  #Index 0
itemno = 567  #Index 1
price = 49.95 #Index 2
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))



