import re

string = input()
pattern = r"[ ,.]"
x = re.sub(pattern, ":", string)
print(x)