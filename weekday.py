# This program outputs whether or not today is a weekday.

# import datetime library [1]
from datetime import datetime


# create a function
def check_if_weekend():
    # datetime.now().weekday() returns the day of the 
    # week represented by an integer 
    # 0 is Monday, 1 in Tuesday, ... , 6 is Sunday
    
    # store day integer in a variable
    i = datetime.now().weekday()
    
    # print name of day uings strftime() method [2], [3]
    print(f"Today is {datetime.now().strftime('%A')}")

    # Sat is 5, Sun is 6. Both are > 4
    if i > 4:
        answer = "It is the weekend, yay!"
        return answer
    # if it is not, then the else part runs
    else:
        answer = "Yes, unfortunately today is a weekday."
        return answer


# create main() function [4], [5]
def main():
    # call the function
    is_weekend = check_if_weekend()
    print(is_weekend)

if __name__ == "__main__":
    main()


'''
[1] https://docs.python.org/3/library/datetime.html
[2] https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
[3] https://www.geeksforgeeks.org/python-strftime-function/
[4] https://realpython.com/if-name-main-python/
[5] https://www.youtube.com/watch?v=g_wlZ9IhbTs&t=103s

'''