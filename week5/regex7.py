import re

string = input()
pattern = r"\b[a-z]+_[a-z]+\b]"
x = re.split("_", string)
my_case = x[1].capitalize()
print(x[0]+my_case)