#!/usr/bin/env python3

#Exercise 8

for i in range(1,101):
    print(i)

#Exercise 9

my_list0_99 = list(range(0,100))
my_list1_100 = list(range(1,101))

for i in my_list0_99+my_list1_100:
    print(i)