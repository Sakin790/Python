#The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper()) # HELLO, WORLD!

#The lower() method returns the string in lower case:
print(a.lower()) # hello, world!

#The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Replace String
name = "Mahid islam"
print(name.replace("Mahid", "sakin")) # [kake remove korbo , ki dibo]

# Split String
score = "I Need Some Money"
print(score.split(" ")) # ['I', 'Need', 'Some', 'Money']

#capitalize
const = "hello"
print(const.capitalize()) # first charector capital hobe

#casefold()
score1= "ATTACK"
print(score1.casefold()) # attack

#encode()
print(score1.encode()) # binary encoded version

#endwith() 
txt = "Hello, welcome to my world."
x = txt.endswith(".") # (.) diye end hosse kina
print(x)

#Find() Kothai welcome ache?
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x) #7
print(txt.find("e")) #1



age = 36
score = 52
txt = f"My name is John, I am {age} and my score is {score}"
print(txt)

age = 36
score = 52
txt = f"My name is John, I am {age:.4f} and my score is {score*2}"
print(txt)