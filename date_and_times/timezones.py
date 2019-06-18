import datetime
import pytz

pacific = datetime.timezone(datetime.timedelta(hours=-8))
eastern = datetime.timezone(datetime.timedelta(hours=-5))

naive = datetime.datetime(2014, 4, 21, 9)
aware = datetime.datetime(2104, 4, 21, 9, 0, tzinfo=pacific)

# naive.astimezone(eastern)  doesn't work
aware.astimezone(eastern)       # returns 12:00

mumbai = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
aware.astimezone(mumbai)        # returns 22:30

# PYTZ
pacific = pytz.timezone('US/Pacific')
eastern = pytz.timezone('US/Eastern')
fmt = '%Y-%m-%d %H:%M:%S %Z%z'
utc = pytz.utc

start = pacific.localize(datetime.datetime(2014, 4, 21, 9))         # localize is for naive times
start.strftime(fmt)         # returns '2014-04-21 09:00:00 PDT-0700'

start_eastern = start.astimezone(eastern)
start_utc = datetime.datetime(2014, 4, 21, 1, tzinfo=utc)
auckland = pytz.timezone('Pacific/Auckland')
mumbai = pytz.timezone('Asia/Calcutta')
apollo_13_naive = datetime.datetime(1970, 4, 11, 14, 13)
apollo_13_eastern = eastern.localize(apollo_13_naive)
apollo_13_utc = apollo_13_eastern.astimezone(utc)
apollo_13_utc.astimezone(auckland(fmt))

pytz.all_timezones          # list of all timezones
pytz.country_timezones['us']        # timezones for that country
