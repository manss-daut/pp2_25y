#just if, elif, else as in c++
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#short one statement
if a > b: print("a is greater than b")
#or ternary operator
a = 2
b = 330
print("A") if a > b else print("B")
#also
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
#and we can use and, or, not in if..else
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
#or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
#not
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
#if can be in if
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")