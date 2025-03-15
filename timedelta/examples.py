# Import Necessary Modules
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

time_delt1 = timedelta(days= 270, hours = 9, minutes = 18)
print(time_delt1)

# Sample Output: 270 days, 9:18:00

# to create reference, use current date and time
time_now = datetime.now()
print(time_now)

# check what date it'll be after time_delt1
future_date1 = time_now + time_delt1
print(future_date1)

# What day will it be after 189 days
future_date2 = time_now + timedelta(days=189)
print(future_date2)

# What day would it have been 189 days ago
past_date1 = time_now - timedelta(days=189)
print(past_date1)

# create reference objects for today, and teachers' day
teachers_day = date(time_now.year, 9, 5)
today = date.today()

# calculate number of days to teachers' day.
time_to_td = teachers_day - today
print(f"Teachers' day is {time_to_td.days} days away")

# check if teachers' day has passed
if teachers_day < today:
  print(f"This year's Teachers' Day was {(today-teachers_day).days} days ago")
  time_to_td = teachers_day - today
  print(f"Next year's Teachers' day is {time_to_td.days} days away")
