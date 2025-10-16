#!/usr/bin/env python3

#Exercise 10

import sys
min = int(sys.argv[1])
max = int(sys.argv[2])

for i in range(min, max+1):
    print(i)

#Exercise 11
import sys
min = int(sys.argv[1])
max = int(sys.argv[2])
my_list = list(range(min,max+1))

for i in my_list:
    print(i)

#Exercise 12
import sys
min = int(sys.argv[1])
max = int(sys.argv[2])

my_list1 =[]
for i in range(min, max+1):
    if int(i)%2 != 0:
        my_list1.append(i)
print(my_list1)