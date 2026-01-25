"""
What is a String:-

A string is an immutable sequence of characters enclosed in:

Single quotes ' '
Double quotes " "
Triple quotes ''' ''' or """ """

"""

s1 = 'Hello'
s2 = "Python"
s3 = """Multi-line
string"""
print(s1)

#String Immutability

s = "hello"
# s[0] = 'H'   # ❌ TypeError

s = "H" + s[1:]
print(s)      # Hello


#Indexing

s = "Python"
print(s[0])    # P
print(s[-1])   # n

#Slicing

s = "Programming"
print(s[0:6])    # Progra
print(s[::2])    # Pormig
print(s[::-1])   # gnimmargorP
print(s[1:4])  # yth


#String Operators:

#Concatenation

a = "Hello"
b = "World"
print(a + " " + b)

#Repetition

print("Hi " * 3)

#Membership

print("Py" in "Python")     # True
print("Java" not in "Python") # True


#Built-in String Functions:

s = "python programming"

print(len(s))
print(sorted(s))


#String Methods:

s = "Python"
print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())
print(s.swapcase())
print(s.count('o'))

#Searching

s = "python programming"
print(s.find("pro"))     # 7
print(s.index("python"))
print(s.count("p"))


#Checking Methods:

s = "Python123"
print(s.isalpha())
print(s.isdigit())
print(s.isalnum())
print(s.startswith("Py"))
print(s.endswith("123"))

#Modification Methods:

s = "   hello world   "

print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s.replace("world", "Python"))

#Splitting and Joining

s = "apple,banana,orange"
lst = s.split(",")
print(lst)

print("-".join(lst))
