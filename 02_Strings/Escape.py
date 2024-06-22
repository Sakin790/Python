txt = "We are the so-called \"Vikings\" from the north."
print(txt)

backslash = "We are the so-called \\Vikings from the north."
print(backslash) # remove one backslash

# \n \r \t \b \f 


s = "hello world"
print(s.capitalize())  # Output: "Hello world"

# casefold()
s = "Hello World"
print(s.casefold())  # Output: "hello world"

# center()
s = "hello"
print(s.center(11, '-'))  # Output: "---hello---"

# count()
s = "hello world"
print(s.count('o'))  # Output: 2

# encode()
s = "hello"
print(s.encode())  # Output: b'hello'

# endswith()
s = "hello world"
print(s.endswith('world'))  # Output: True

# expandtabs()
s = "hello\tworld"
print(s.expandtabs(4))  # Output: "hello   world"

# find()
s = "hello world"
print(s.find('o'))  # Output: 4

# format()
s = "Hello, {}!"
print(s.format("world"))  # Output: "Hello, world!"

# format_map()
s = "Hello, {name}!"
print(s.format_map({'name': 'world'}))  # Output: "Hello, world!"

# index()
s = "hello world"
print(s.index('o'))  # Output: 4

# isalnum()
s = "hello123"
print(s.isalnum())  # Output: True

# isalpha()
s = "hello"
print(s.isalpha())  # Output: True

# isascii()
s = "hello"
print(s.isascii())  # Output: True

# isdecimal()
s = "12345"
print(s.isdecimal())  # Output: True

# isdigit()
s = "12345"
print(s.isdigit())  # Output: True

# isidentifier()
s = "variable1"
print(s.isidentifier())  # Output: True

# islower()
s = "hello"
print(s.islower())  # Output: True

# isnumeric()
s = "12345"
print(s.isnumeric())  # Output: True

# isprintable()
s = "hello"
print(s.isprintable())  # Output: True

# isspace()
s = "   "
print(s.isspace())  # Output: True

# istitle()
s = "Hello World"
print(s.istitle())  # Output: True

# isupper()
s = "HELLO"
print(s.isupper())  # Output: True

# join()
s = "-"
seq = ("a", "b", "c")
print(s.join(seq))  # Output: "a-b-c"

# ljust()
s = "hello"
print(s.ljust(10, '-'))  # Output: "hello-----"

# lower()
s = "HELLO"
print(s.lower())  # Output: "hello"

# lstrip()
s = "   hello"
print(s.lstrip())  # Output: "hello"

# maketrans() and translate()
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
s = "this is a test"
print(s.translate(trantab))  # Output: "th3s 3s 1 t2st"

# partition()
s = "hello world"
print(s.partition(' '))  # Output: ('hello', ' ', 'world')

# replace()
s = "hello world"
print(s.replace('world', 'there'))  # Output: "hello there"

# rfind()
s = "hello world"
print(s.rfind('o'))  # Output: 7

# rindex()
s = "hello world"
print(s.rindex('o'))  # Output: 7

# rjust()
s = "hello"
print(s.rjust(10, '-'))  # Output: "-----hello"

# rpartition()
s = "hello world"
print(s.rpartition(' '))  # Output: ('hello', ' ', 'world')

# rsplit()
s = "hello world"
print(s.rsplit(' '))  # Output: ['hello', 'world']

# rstrip()
s = "hello   "
print(s.rstrip())  # Output: "hello"

# split()
s = "hello world"
print(s.split(' '))  # Output: ['hello', 'world']

# splitlines()
s = "hello\nworld"
print(s.splitlines())  # Output: ['hello', 'world']

# startswith()
s = "hello world"
print(s.startswith('hello'))  # Output: True

# strip()
s = "   hello   "
print(s.strip())  # Output: "hello"

# swapcase()
s = "Hello World"
print(s.swapcase())  # Output: "hELLO wORLD"

# title()
s = "hello world"
print(s.title())  # Output: "Hello World"

# upper()
s = "hello"
print(s.upper())  # Output: "HELLO"

# zfill()
s = "42"
print(s.zfill(5))  # Output: "00042"
