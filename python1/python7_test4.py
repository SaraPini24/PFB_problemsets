#!/usr/bin/env python3

#Exercise 9, 10

import re
import sys
enzyme = sys.argv[1]
sequence = sys.argv[2]

#Creating the dictionary {enzyme : restriction site}
count = 0
dictionary = {}

with open('bionet.txt', 'r') as restrictions:
    for line in restrictions:
        line = line.rstrip()
        line = re.sub(r'(\S+)( +)?(\S+)( +)(\S+)', r'\1\3 \5', line)
        count+=1
        if count >= 11: #from line 10 to exclude header
            if len(line) != 0:
                new = line.split(' ')
                #print(new)
                dictionary[new[0]] = new[1]


#Parse the FASTA file
parsed = {}
with open(sequence, 'r') as fasta:
    for line in fasta:
        line = line.rstrip()
        if line.startswith('>'):
            for match in re.finditer(r'^(>\S+)(.+)?', line):
                name_seq = match.group(1).lstrip('>')
                parsed[name_seq] = ''
        else:
            parsed[name_seq] = parsed[name_seq] + line

#read the file provided and look for restriction sites of the enzyme provided
    if enzyme in dictionary: #if the enzye name provided is in the dictionary keys
        for seq in parsed: #for each sequence in the fasta file
            seq_with_rest = re.sub(re.sub(r'\^','',dictionary[enzyme]),dictionary[enzyme], parsed[seq])
            fragments = re.sub(re.sub(r'\^','',dictionary[enzyme]),dictionary[enzyme], parsed[seq]).split('^')
            n_fragments = len(re.sub(re.sub(r'\^','',dictionary[enzyme]),dictionary[enzyme], parsed[seq]).split('^'))
            print(f'Restriction pattern: {seq_with_rest}') #prnt the sequence with ^ at restriction sites
            print(f'Number of fragments: {n_fragments}')
            print(f'Fragments in natural order: {fragments}')
            print(f'Fragments sorted by length: {sorted(fragments, reverse=True)}')

    