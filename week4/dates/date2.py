import datetime
from datetime import timedelta
today = datetime.datetime.now()
yesterday = today - timedelta(days = 1)
tomorrow = today + timedelta(days = 1)
print(yesterday)
print(today)
print(tomorrow)