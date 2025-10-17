#!/usr/bin/env python3

#Exercise 1

import re

line_n = 0
with open('Python_07_nobody.txt', 'r') as nobody:
    for line in nobody:
        line_n += 1
        for f in re.finditer(r'Nobody', line):
            whole = f.group(0)
            start = f.start()+1
            end = f.end()
            if f:
                print(whole, line_n, start, end) #cosi stampa solo le righe in cui trova un match altrimenti stamperebbe con il numero della riga aumentato e whole start ed end dell-ultimo match

#Exercise 2

import re
with open('Python_07_nobody.txt', 'r') as nobody, open('Michael.txt', 'w') as fo:
    for line in nobody:
        new_line = re.sub(r'Nobody', 'Michael', line)
        fo.write(new_line)
