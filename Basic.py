import datetime as dt

now = dt.datetime.now()
print("Now:", now)

today = dt.date.today()
print("Today:", today)

current_time = dt.datetime.now().time()
print("Time:", current_time)

d = dt.date(2023, 5, 5)
t = dt.time(14, 30, 15)

print("Datetime :", dt.datetime(2023, 5, 5, 14, 30, 15))

today = dt.date.today()
delta = dt.timedelta(days=10)

future = today + delta
past = today - delta

print("10 days later:", future)
print("10 days ago:", past)

now = dt.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # Custom format

date = dt.date(2023, 5, 5)
time = dt.time(14, 30)
combined = dt.datetime.combine(date, time)          

print("Combined datetime:", combined)

now = dt.datetime.now()
updated = now.replace(hour=0, minute=0)
print("Midnight today:", updated)
