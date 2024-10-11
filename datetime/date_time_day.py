import datetime

d = datetime.date(2024, 10,11)
dd = datetime.date.today()
today_day = datetime.date.today()
print(d)
print(dd)
print(today_day)
print(today_day.weekday()) #monday is 0 sunday is 6
print(today_day.isoweekday()) #mosday is 1 sunday is 7

"""Time Delta are difference between 
two dates or time used to do operations on dates or time"""

today_delta = datetime.timedelta(days=7)
print(today_day + today_delta) #to know what date it will be 7 days from now
print(today_day - today_delta) # to know what date it was 7 days ago

# date2 = date1 + timedelta
# timedelta = date1 + date2