import datetime

x = datetime.datetime.now()
print(dir(datetime))
print(x.year)
print(x.strftime("%A"))

x = datetime.datetime(2020, 1, 17)
print(x.year)
print(x.month)
print(x.strftime("%B"))
print(x.strftime("%b"))