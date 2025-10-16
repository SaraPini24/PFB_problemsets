#!/usr/bin/env python3

#Exercise 1 and 2

with open('python_06.txt', 'r') as text_obj, open('python_06_uc.txt', 'w') as write_obj:
    for line in text_obj:
        line = line.rstrip().upper()
        write_obj.write(f'{line}\n')

#The putput is written in the file. So when you run the code nothing will appear on the screen