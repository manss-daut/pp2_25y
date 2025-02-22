import re

string = input()
pattern = r"[A-Z][a-z]+"
x = re.findall(pattern, string)
print(x)
#similar to 4th task