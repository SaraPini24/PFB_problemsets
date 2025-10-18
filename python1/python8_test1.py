#!/usr/bin/env python3

#Exercise 2, 3

import sys
import re

sequence = sys.argv[1]

#Parsing FASTA file
parsed = {}

with open(sequence, 'r') as fasta:
    for line in fasta:
        line = line.rstrip()
        if line.startswith('>'):
            for match in re.finditer(r'^(>\S+)(.+)?', line):
                name_seq = match.group(1).lstrip('>')
                parsed[name_seq] = {}
                parsed[name_seq]['sequence'] = ''

        else:
            parsed[name_seq]['sequence'] = parsed[name_seq]['sequence'] + line

with open('Python_08.codons-frame-1.nt.txt', 'w') as fo:
    for name_seq in parsed:
        codons = re.findall(r'(.{3})',parsed[name_seq]['sequence']) #Identifies codon from frame 1
        fo.write(f'seq{name_seq}-frame1-codons\n')
        for codon in codons:
            fo.write(f'{codon} ')
        fo.write('\n')


#Getting the codons from the 3 frames on fw strand
with open('Python_08.codons-frame-1_3.nt.txt', 'w') as fo:
    for name_seq in parsed:
        for n in range(3):
            codons = re.findall(r'(.{3})',parsed[name_seq]['sequence'][n:]) #Identifies codon from frame 1
            fo.write(f'seq{name_seq}-strand + frame{n+1}-codons\n')
            for codon in codons:
                fo.write(f'{codon} ')
            fo.write('\n')


#Getting the codons from the 3 frames on rv strand
#make rev compl
translation_tab = str.maketrans('ACTG', 'TGAC')
for name_seq in parsed:
    seq_rev = parsed[name_seq]['sequence'][::-1]
    seq_rev_compl = seq_rev.translate(translation_tab)
    parsed[name_seq]['revcompl']= seq_rev_compl

#get codons
with open('Python_08.codons-strand- frame-1_3.nt.txt', 'w') as fo:
    for name_seq in parsed:
        for n in range(3):
            codons = re.findall(r'(.{3})',parsed[name_seq]['revcompl'][n:]) #Identifies codon from frame 1
            fo.write(f'seq{name_seq}-strand - frame{n+1}-codons\n')
            for codon in codons:
                fo.write(f'{codon} ')
            fo.write('\n')