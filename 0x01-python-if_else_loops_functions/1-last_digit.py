#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
oderRange = ""

if (last_digit > 5):
    oderRange = "greater than 5"
elif (last_digit == 0):
    oderRange = "0"
else:
    oderRange = "less than 6 and not 0"
