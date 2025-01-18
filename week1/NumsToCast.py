#in py numbers there are 3 types:
x = 3
y = 2.2
z = 3j
print(type(x))
print(type(y))
print(type(z))

#we can change them bt own choise like:
#from int to float:
x1 = float(x)
print(x1)
#from float to complex:
y2 = complex(y)
print(y2)
#we can't from complex to another
#we can change as we write and type will be same every time after change
x2 = float(1)     # x will be 1.0
y2 = float(2.8)   # y will be 2.8
z2 = float("3")   # z will be 3.0
w2 = float("4.2") # w will be 4.2
print(type(x2))
print(type(w2))
x3 = str("s1") # x will be 's1'
y3 = str(2)    # y will be '2'
z3 = str(3.0)  # z will be '3.0'