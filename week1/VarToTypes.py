x = 5
y = "John"
print(x)
print(y)
z = str(12)
print(z)
#i can change variables like:
x = "Sally"
#and print last one
print(x)

#illegal variables
"""
2myvar = "John"
my-var = "Daut"
my var = "Mans

"""
x1, y1, z1 = "BMW", "Mercedes", "Volvo"
print(x1, y1, z1)
# "," means a space in output
#print(x1 + y1 + z1) will put in one row, so:
x1 = "C++"
y1 = "is"
z1 = "Great"
print(x1 + y1 + z1)

#i can take it directly? from array
fruits = ["apple", "banana", "pineapple"]
x2, y2, z2 = fruits
print(x2)
print(y2)
print(z2)

#numbers in with "+" in  output will give the sum, and so can be made other operations
x3 = 12
y3 = 3
print(x3 + y3)

#variables outside func mean global vars
x4 = "bomba"
def myfunc():
    print("DOTA 2 is " + x4)
myfunc()

#if i name my var in func it will be so only in func
x5 = "great"
def myfunc():
   x5 = "bad"
   print("FIFA 25 " + x5)
myfunc()
print("FIFA 25 " + x5)

#also i can name vars as global
x6 = "great"
def myfunc():
   global x6
   print("FIFA 25 " + x6)
myfunc()
print("FIFA 25 " + x6)

#to get the variables type write:
print(x3)
print(y)
print(type(x3))
print(type(y))