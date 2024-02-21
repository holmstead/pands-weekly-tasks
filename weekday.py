# This program outputs whether or not today is a weekday.

from datetime import datetime

# define a list of the days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# use *args to unpack the list
#print(*days)

# print the current date and time
#print(f'Datetime is: {datetime.now()}')

# print the day of the week represented by an integer
# 0 is Monday, 1 in Tuesday, ... , 6 is Sunday
#print(f'Today as an integer: {datetime.now().weekday()}')

# use index to access the day in the list
i = datetime.now().weekday()
print(f"Today is {days[i]}")

weekend = ["Saturday", "Sunday"]

today = days[i]

# ckeck the 'weekend' list if today is in it
if today in weekend:
    print("It is the weekend, yay!")
# if it is not, then the else part runs
else:
    print("Yes, unfortunately today is a weekday.")