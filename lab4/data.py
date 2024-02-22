#ex1
import datetime

x = datetime.datetime.now() - datetime.timedelta(days=5)
print(x.strftime("%d"))


#ex2
import datetime
today = datetime.datetime.now() 
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print(today.strftime("%d"))
print(yesterday.strftime("%d"))
print(tomorrow.strftime("%d"))

#ex3
import datetime
today = datetime.datetime.now()
drop_micr = today.replace(microsecond=0)
print(drop_micr)

#Ex4
import datetime
today = datetime.datetime.now()
another_day = today + datetime.timedelta(days=5)
diff = another_day - today
print(diff.total_seconds())
