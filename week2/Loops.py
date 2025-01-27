#for while we need increment
i = 1
while i < 6:
  print(i)
  i += 1
print("\n")
#to break statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
print("\n")
#or continue, jump over some
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
print("\n")
#can be messaged by end or else
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
print("\n")
#For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#through string
for x in "banana":
  print(x)
#as in while to stop use break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#same continue to skip some value
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#can loop through some range, but last is num before
for x in range(2, 6):
  print(x)#from 2 to 5
#from one to another by some move
for x in range(2, 30, 3):
  print(x)#from 2 to 30 by 3 - 2,5,8...29
#message as else in loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")
#nested loop for in for
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)