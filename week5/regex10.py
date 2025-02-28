import re

camelCase = input()
pattern = r'[A-Z][a-z]*|[a-z]+'
x = re.findall(pattern, camelCase)
my_case = ""
for i in range(len(x)):
    if i > 0:
        my_case += "_"
    my_case += x[i].lower()
print(my_case)