#!/usr/bin/env python3

#Exercise 6, 7, 8 - identification of restriction sites
import re

with open('Python_07_ApoI.fasta.txt', 'r') as fasta:
    for line in fasta:
        for match in re.finditer(r'([AG])(AATT[CT])',line):
            whole = match.group(0)
            start = match.start()+1
            end = match.end()

            print(f'Motif: {whole}, Cut: {match.group(1)}^{match.group(2)}, Start: {start}, End: {end}')


#print the whole sequence with ^ at restriction sites
new_fasta = ''
with open('Python_07_ApoI.fasta.txt', 'r') as fasta:
    for line in fasta:
        line = line.rstrip()
        for match in re.finditer(r'([AG])(AATT[CT])',line):
            line = re.sub(r'([AG])(AATT[CT])',r'\1^\2',line)
            #print(line)
            new_fasta = new_fasta+line
#print(new_line)
r_fragment = new_fasta.split('^')
#print(r_fragment)
r_fragment_sort = sorted(r_fragment, key=len)
print(r_fragment_sort)
