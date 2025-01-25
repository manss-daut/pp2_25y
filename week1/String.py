a = "Hello"
print(a)
#we can get the character at position 1
a = "Hello, World!"
print(a[1])
#we can frm one position to another
b = "Whats up"
print(b[2:5])
#or before some point
print(b[:5])
#or from some point
print(b[2:])
#or we can do it from left
print(b[-5:-2])
#string in upper case, or lower case:
c = "The best"
print(c.upper())
print(c.lower())
#we can replce any letters we want
d = "Honored one"
print(d.replace("H", "J"))
#we can split string into two substrings
e = "The worlds first rocket"
print(e.split(" "))
#concatination
a = "Hello"
b = "World"
c = a + b
print(c)
#or like this with a space
a = "Hello"
b = "World"
c = a + " " + b
print(c)
#we can loop through the characters in a string
for x in "banana":
  print(x, end = '')
#lenght of a string
f = """If the world was ending
I'd wanna be next to you
If the party was over
And our time on Earth was through"""
print('\n', len(f))
#we can write string in string
price = 52
txt0 = f"The price is {price} dollars"
print(txt0)
#by 2 decimals
txt1 = f"The price is {price:.2f} dollars"
print(txt1)
#also can be math
txt2 = f"The price is {20 * 59} dollars"
print(txt2)
