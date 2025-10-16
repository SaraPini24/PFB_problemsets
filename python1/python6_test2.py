#!/usr/bin/env python3

#Exercise 4
n_lines = 0
n_ID = 0
n_char = 0
n_nt = 0
n_nt_lines = 0

with open('Python_06.fastq.txt', 'r') as fastq_seq:
    for line in fastq_seq: #for each linein the fastq
        n_lines += 1 #add one to the count of lines
        n_char = n_char+len(line.rstrip()) #add as many characters are in line (without the final \n character)
        if '@HWI' in line: #looks for ID lines
            n_ID = n_ID+1 #counts the number of ID lines
        if n_lines%4 ==2: #identifies all lineas with nt (2, 6, 10 ecc)
            n_nt_lines += 1
            n_nt = n_nt+len(line.rstrip()) #add as many characters are in nt line (without the final \n character)   

print(f'Total number of lines: {n_lines}\nTotal number of characters: {n_char}\nTotal number of nt: {n_nt}\nTotal number of IDs: {n_ID}\nAverage line length: {n_char/n_lines:g}\nAverage nt line length: {n_nt/n_nt_lines:g}')
