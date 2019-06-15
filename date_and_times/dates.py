import datetime

treehouse_start = datetime.datetime.now()
treehouse_start = treehouse_start.replace(hour=9, minute=0, second=0, microsecond=0)

time_worked = datetime.datetime.now() - treehouse_start   
# returns datetime.timedelta(0, 33972, 762540) -> days, seconds, microseconds

time_worked.days    # returns 0
time_worked.seconds # returns 33972
time_worked.microsecond # returns 762540
hours_worked = round(time_worked/3600)

# delta
treehouse_start + datetime.timedelta(days=3)
treehouse_start + datetime.timedelta(days=-5)   # goes back 5 days
treehouse_start - datetime.timedelta(days=5)

now = datetime.datetime.now()
now.date()  # returns (2019, 6, 14)
now.time()  # returns (19, 47, 1, 456347)

hour = datetime.timedelta(hours=1)
workday = hour * 9
tomorrow = datetime.datetime.now().replace(hour=9, minute=0) + datetime.timedelta(days=1)
tomorrow + workday  # returns when work will end tomorrow

today = datetime.datetime.today()
today.weekday()     # 0 - Monday, 1 - Tuesday ...

now.timestamp()     # the POSIX timestamp for now

# strftime - Method to create a string from a datetime 
# strptime - Method to create a datetime from a string according to a format string
# https://docs.python.org/3/library/datetime.html?highlight=datetime#strftime-and-strptime-behavior

now.strftime('%m/%d/%y')     # returns '06/14/19'
now.strftime('%B %d')       # returns 'June 14'

birthday = datetime.datetime.strptime('2015-04-21', '%Y-%m-%d')     # returns datetime.datetime(2015, 4, 21, 0, 0)
birthday_party = datetime.datetime.strptime('2015-04-21 12:00', '%Y-%m-%d %H:%M')   

