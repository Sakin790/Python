name= ["Sakin", "Tamim","Abir"]
for x in name:
        print(x)


mix= [True, 12,"Score"]
for y in mix:
        print(y)
        
# Via index   
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  

score = [100, 200, 300, 400]
length= len(score) # 4
i = 0
while i < length:
        print(score[i])
        i= i+1


thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
