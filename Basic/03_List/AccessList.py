score = [100,200,300,400,500]
print(score[0]) #  100
print(score[-1]) #  500

ChangeScore = score[0] = 200
print(ChangeScore)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #  "banana", "cherry", "orange", "kiwi"


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:5]) # Till 5

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

if "banana" in thislist:
        print("yes !, im in") # True