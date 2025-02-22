import re

string = input()
pattern = r"^ab{2,3}$"
x = re.match(pattern, string)
if x: 
    print("Yes")
else: 
    print("No")