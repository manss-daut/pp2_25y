import datetime
from datetime import timedelta
cur = datetime.datetime.now()
bef = cur - timedelta(days = 5)
print(bef)#.strftime("%A"))