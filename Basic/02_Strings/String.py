#Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


# String are Simillar to Array , Array te ja ja method use kora jeto
# String eu ogulo kora jabe like [For loop]

name = "Jhon Stone"
print(name[1]) # h
print(name[-1]) # e
print(len(name)) # 10 , [With Space]

# For loop
for x in "banana":
  print(x) 

#Check String // String er moddhe kono Word ache kina
text = "I Love Bangladesh"
result = "Love" in text
print(result)


txt = "The More You Fair The More Will Happen"
if "Fair" in txt :
  print("Yes! , Fair in present")
