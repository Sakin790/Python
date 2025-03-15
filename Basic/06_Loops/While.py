count = 0
list= [12,25,88,55,66,55,88]

while count<len(list):
    print(f"Value is {list[count]}")
    count += 1

# Fina value in tuple 
list=[88,55,88,22,333,00,44,55,45,31,54,]
x= 55
count= 0
while  count < len(list):
    if(list[count] == x):
        print("Value Match")
        count += 1
    else:
        print("X Not Found")
        count += 1

#--------------------------------------
list=[88,55,88,22,333,00,44,55,45,31,54,]
x= 55
count= 0
while  count < len(list):
    if(list[count] == x):
        print("Value Match")
        break
    else:
        print("X Not Found")
        count += 1
#Break and (Continue=>For skip any value)


j=0
while j<= 5:
    if(j==3):
      j+=1
      continue
    print(j)
    j+=1 

#---------------
i= 1
while i<=10:
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1

i= 1
while i<=10:
    if(i%2!=0):
        i+=1
        continue
    print(i)
    i+=1