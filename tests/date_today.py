import datetime

today = datetime.datetime.now()
date = today.strftime('%d.%m')
time = today.strftime('%H:%M:%S')
hours = int(today.strftime('%H'))

print(hours)

x = list(range(0, 10))
print(x)
