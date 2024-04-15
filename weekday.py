# This program outputs whether or not today is a weekday.

# import datetime library
from datetime import datetime


# create a function
def check_if_weekend():
    # datetime.now().weekday() returns the day of the 
    # week represented by an integer 
    # 0 is Monday, 1 in Tuesday, ... , 6 is Sunday
    
    # store day integer in a variable
    i = datetime.now().weekday()
    
    # print name of day using strftime() method
    print(f"Today is {datetime.now().strftime('%A')}")

    # Sat is 5, Sun is 6. Both are > 4
    if i > 4:
        answer = "It is the weekend, yay!"
        return answer
    # if it is not, then the else part runs
    else:
        answer = "Yes, unfortunately today is a weekday."
        return answer


# create main() function
def main():
    # call the function
    is_weekend = check_if_weekend()
    print(is_weekend)

if __name__ == "__main__":
    main()