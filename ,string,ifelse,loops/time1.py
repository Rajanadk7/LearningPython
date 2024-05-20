import time
timestamp= time.strftime('%H:%M:%S')
print(timestamp)
timestamp= time.strftime('%H')
print(timestamp)
timestamp= time.strftime('%M')
print(timestamp)
timestamp= time.strftime('%S')
print(timestamp)
if time.strftime('%H:%M:%S')>=('22:00:00')or time.strftime('%H:%M:%S')<=('06:00:00'):
     print("goood night")
elif time.strftime('%H:%M:%S')>=("06:00:00")or time.strftime('%H:%M:%S')<=('12:00:00'):
     print('good morning')
elif time.strftime('%H:%M:%S')>=("12:00:00")or time.strftime('%H:%M:%S')<=('06:00:00'):
     print('good afternoon')