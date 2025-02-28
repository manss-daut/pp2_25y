import re

string = input()
pattern = r'(?<!^)(?=[A-Z])'
result = re.sub(pattern, ' ', string)
print(result)
