#!/usr/bin/env python3

#Exercise 1

import sys
import re

sequence = sys.argv[1]

#Parse the FASTA file
parsed = {}
dataset = {}
with open(sequence, 'r') as fasta:
    for line in fasta:
        line = line.rstrip()
        if line.startswith('>'):
            for match in re.finditer(r'^(>\S+)(.+)?', line):
                name_seq = match.group(1).lstrip('>')
                parsed[name_seq] = ''
        else:
            parsed[name_seq] = parsed[name_seq] + line

#Creating a new dataset (dictionary of dictionaries) {name:{sequence:'ACTG',nt_count{A:nnn,T:nnn,C:nnnn,G:nnnn}}}
for name_seq in parsed:
    dataset[name_seq]= {}
    dataset[name_seq]['Sequence'] = parsed[name_seq]
    x = dataset[name_seq]['Sequence']
    dataset[name_seq]['nt_count'] = {}
    dataset[name_seq]['nt_count']['A'] = x.count('A')
    dataset[name_seq]['nt_count']['C'] = x.count('C')
    dataset[name_seq]['nt_count']['G'] = x.count('G')
    dataset[name_seq]['nt_count']['T'] = x.count('T')

print(f'seqName\tA_count\tT_count\tG_count\tC_count')
for name_seq in dataset:
    print(f'{name_seq}\t{dataset[name_seq]['nt_count']['A']}\t{dataset[name_seq]['nt_count']['T']}\t{dataset[name_seq]['nt_count']['G']}\t{dataset[name_seq]['nt_count']['C']}')

