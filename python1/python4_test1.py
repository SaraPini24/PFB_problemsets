#!/usr/bin/env python3

#Exercise 4: while loop to sum al numbers from 1 to 100
i = 0
sum = 0
while i<100:
    i=i+1
    sum = sum+i
print(sum)

#Exercise 5: while loop to calculate the factorial of 10
i=0
fact10=1
while i<10:
    i=i+1
    fact10=fact10*i
print(fact10)

#Exercise 6 and 7
numbers = [101,2,15,22,95,33,2,27,72,15,52]

for number in numbers:
    if int(number)%2 == 0:
        print(number)

numbers_sort = sorted(numbers)
#print(numbers_sort)
sum_even=0
sum_odd=0
for number in numbers_sort:
    print(number)
    if int(number)%2 == 0:
        sum_even=sum_even+int(number)
    else:
        sum_odd=sum_odd+number
print(f'Sum of even numbers = {sum_even}\nSum of odd numbers = {sum_odd}')