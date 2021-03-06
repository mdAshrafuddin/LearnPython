# Variabler are a containers for storing data value
# A Variable reserved memory location
"""
    Basic data type
    string
    integer
    float
    bo9lean
""" 
"""
    Must start with a letter or ubderscore character
    Can not start with number
    Can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )  
    Variable names are case-sensitive (age and Age deference)
"""

# Declaration of Variables
x = 5
y = "AShraf Uddin"

print(x)
print(y)

# Integers example 2. ,3, 5, 6
aIn = 2
bIn = 3

type(aIn),  type(bIn)
print(aIn+bIn)

# Float exmaple 33.33 44.4
aFl = 33.44
bFl = 45.4
i = 1

print(type(i + aFl))
print(type(aFl))
print(type(bFl))
print(aFl + bFl)

# Math functions
"""
    abs() Returns absolute value of a number
    pow() Raises a number to a power
    round() Rounds a floating-point value
"""
res = pow(3, 2)
print(abs(-2))
print(res)
print(round(3.14, 1))

# Strings
s1 = "AShraf"
s2 = "Tanjil"
print(s1 + s2)

aS = 1
print(f"I am string with an int here {aS + 2} - and more text")

# Boolean True or flase
aB1 = True
aB2 = False
print(aB1)
print(aB2)

# Casting
a = int(3.4)
b = float(3)

print(a)
print(b)

# Get the Type
n = "String"
m = 10

print(type(n))
print(type(m))

# Single or Double Quotes

print('AShraf')
print("Tanjil")

# Case-Sensitive
z = 30
Z = 39
print(z)
print(Z)

# Legal variable names:
myvar = "AShraf"
my_var = "AShrfa"
_my_var = "AShrfa"
myVar = "AShraf"
MYVAR = "AShraf"
myvar2 = "AShraf UDdin"

# Illegal variable names:
# 2myvar = "Ashraf"
# my-var = "AShraf"
# my var = "AShraf"

# Multi Words Variable Names

# Camel case
myVariableName = "John"

# Pascal Case
MyVarName = "AShrfa"

# Snake Case
my_var_name = "AShraf"

# Many Values to Multiple Variables
x1, y1, z1 = "Organe", "Banana", "Cherry"

print(x1)
print(y1)
print(z1)

# One Value to Multiple Variables
a1 = b1 = c1 = " AShraf"

print(a1)
print(b1)
print(c1)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x2, y2, z2 = fruits

print(x2)
print(y2)
print(y2)

# Output
x3 = "awesome"
print("Python is " + x3)

# You can also use the + character to add a variable to another variables 
x4 = "Python is "
y4 = "awesome"
z4 =  x4 + y4
print(z4)

# number and string  can not add
# error here
# x6 = 34
# y6 = "AShraf"

# print(x6 + y6)

# Global Variables

x = "Global"

def gloFun():
    print("This is a  ", x)

gloFun()

print("This is a  ", x)

# The global Keyword
def myFun():
    global i
    i = "global variable"

myFun()

print(i)