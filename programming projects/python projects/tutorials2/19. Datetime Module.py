import datetime
import pytz

#output will be the date today
today = datetime.date.today()
print(today)

#assigning an event or date
birthday = datetime.date(2003, 12, 26)
print(birthday)

#find day since birth
days_since_birth = (today - birthday).days
print(days_since_birth)

#to add or even to subract the current date
#adding 10 days to current day
tdelta = datetime.timedelta(days=10)
print(today + tdelta)

print(today.month)
print(today.day)

# tuesday = 1
print(today.weekday())
#monday = 0, sunday = 6

print(datetime.time(7, 2, 20, 15))
#datetime.date(year, month, date)
#datetime.time(hours, minutes, second,microseconds)
#datetime.datetime(year, month date, hourse, minutes, secnd, microseconds)

#add 10 hours to current day
hour_delta = datetime.timedelta(hours=10)
print(datetime.datetime.now() + hour_delta)

#for finding time zones
datetime_today = datetime.datetime.now(tz=pytz.UTC)
datetime_pacific = datetime_today.astimezone(pytz.timezone('US/Pacific'))
print(datetime_pacific)
for tz in pytz.all_timezones:
    print(tz)

#string formatting dates
#2019-03-09 -> March 3, 2019
#strftime (f=formatting)
print(datetime_pacific.strftime('%B %d, %Y'))

#April 15, 2020 -> datetime(2019,4,15)
#strptime (p=parsing)
datetime_thing = datetime.datetime.strptime("April 15,2020", "%B %d, %Y")
print(repr(datetime_thing))







