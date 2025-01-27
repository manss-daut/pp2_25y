#arihmetic 
x = 5
y = 2
a = x + y
b = x - y
c = x / y
d = x * y
#power
e = x ** y
#round down
f = x // y
#for remainder
g = x % y
print(a, b, c, d, e, f, g)
#logical 
#and if both work
print(x > 3 and x < 10)
#if one works
print(x < 3 or x < 10)
#if both works returns false
print(not(x > 3 and x < 10))
#also comparison as in c++
#identity
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is y)
#x is not the same object as y
print(x is z)
print(x == y)
#here the values of x same as y so true
#also we have is not its pretty same but vise versa
print(x is not z)
#and so on
#we have in to check value on something
x = ["apple", "banana"]
print("banana" in x)
#and not in vise versa
x = ["apple", "banana"]
print("pineapple" not in x)
