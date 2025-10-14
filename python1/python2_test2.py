#!/usr/bin/env python3
import sys

test_number = float(sys.argv[1])

print(test_number, 'is the tested number')
if test_number > 0:
    print('it is positive')
    if test_number <= 50:
        print('but smaller than or equal 50')
        if test_number % 2 == 0:
            print('it is an even number that is smaller than or equal 50')
    elif test_number % 3 == 0:
            print('it is larger than 50 and dvisible by 3')
elif test_number < 0:
    print('it is negative')
else:
    print('it must be 0')