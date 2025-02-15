from datetime import datetime
print("First date:")
date1 = input()
date1 = datetime.strptime(date1, "%Y %m %d")
print("Second date:")
date2 = input()
date2 = datetime.strptime(date2, "%Y %m %d")
diff = (date1 - date2).days
answer = diff * 86400
print(answer)