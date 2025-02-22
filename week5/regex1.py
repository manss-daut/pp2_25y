import re

string = input()
pattern = r"^ab*$"
x = re.match(pattern, string)
if x: 
    print("Yes")
else: 
    print("No")