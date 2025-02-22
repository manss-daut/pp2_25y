import re

string = input()
pattern = r"[a-z]+[A-Z]+"
x = re.split("", string)
my_case = x[1].capitalize()
print(x[0]+my_case)