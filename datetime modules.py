import datetime

a = datetime.datetime.now()
print("current date and time: ",a)

b = datetime.date(2019,4,21)
print("user created date: ",b)

c = datetime.time(12,55,50)
print("user created time: ",c)

d = datetime.datetime(2019,4,21,9,55,5)
print("user created date and time: ",d)

e = d.strftime("%Y-%b-%d")
print("formated date: ",e)

