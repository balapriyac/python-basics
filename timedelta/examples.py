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
