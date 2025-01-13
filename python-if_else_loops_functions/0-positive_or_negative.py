#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number > 0:
	print("%s is positive\n" % number)
elif number < 0:
	print("%s is negative\n" % number)
else:
	print("%s is zero\n" % number)
