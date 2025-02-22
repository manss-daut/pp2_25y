import re

string = input()
pattern = r"[A-Z][a-z]+"
x = re.findall(pattern, string)
print(x)