#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = number % 10
message = "Last digit of {:d} is {:d}".format(number, last_digit)
if last_digit > 5:
    message += " and is greater than 5"
elif last_digit == 0:
    message += " and is 0"
else:
    message += " and is less than 6 and not 0"
print(message)
