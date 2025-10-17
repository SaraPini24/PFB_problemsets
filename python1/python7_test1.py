#!/usr/bin/env python3

#Exercise 3, 4

import re
with open('Python_07.fasta.txt', 'r') as fasta:
    for line in fasta:
        #print(line)
        for header in re.finditer(r'^(>\S+)(.+)', line): #match has to START with > and include several characters but spaces and then any character including spaces
            if header:
                print(f'id:{header.group(1).lstrip('>')} desc:{header.group(2)}')
                #if the match exists use the first subse to print the sequence name and the second to print the description


