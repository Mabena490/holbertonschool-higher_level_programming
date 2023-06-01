#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number % 10 == 0:
        print("Last digit of {} is 0 and is 0".format(number))
elif number < 0:
        print("Last digit of {} is {}".format(number, (10 - number % 10) * -1),
