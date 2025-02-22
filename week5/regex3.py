import re

string = input()
pattern = r"\b[a-z]+_[a-z]+\b"
x = re.findall(pattern, string)
print(x)