import re

string = input()
pattern = r"^a.*b$"
x = re.match(pattern, string)
if x: 
    print("Yes")
else: 
    print("No")