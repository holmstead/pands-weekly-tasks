# This program outputs whether or not today is a weekday.

# import datetime library
from datetime import datetime

# define a list of the days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# create a function
def check_if_weekend():
    # datetime.now().weekday() returns the day of the 
    # week represented by an integer 
    # 0 is Monday, 1 in Tuesday, ... , 6 is Sunday
    # use index to access the day in the list
    i = datetime.now().weekday()
    print(f"Today is {days[i]}")

    # Sat is 5, Sun is 6. Both are > 4
    if i > 4:
        answer = "It is the weekend, yay!"
        return answer
    # if it is not, then the else part runs
    else:
        answer = "Yes, unfortunately today is a weekday."
        return answer

print(check_if_weekend())