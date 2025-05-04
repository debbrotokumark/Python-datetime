from datetime import datetime, timedelta
import time

try:
    seconds = int(input("Enter countdown time in seconds: "))
    end_time = datetime.now() + timedelta(seconds=seconds)

    while datetime.now() < end_time:
        remaining = end_time - datetime.now()
        print("Time left:", remaining.seconds, "seconds", end='\r')
        time.sleep(1)

    print("\nTime's up!")
except ValueError:
    print("Please enter a valid number.")
