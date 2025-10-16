#!/usr/bin/env python3

#Extra exercise

dictionary = {}

As=0
Cs=0
Ts=0
Gs=0
tot_len = 0

with open('Python_06.seq.txt', 'r') as sequence:
    for line in sequence:
        line = line.rstrip()
        id,seq = line.split('\t') #split id and sequence for each line and assigning the pieces to two variables
        dictionary[id] = seq #creating the dictionary entry
        tot_len += len(seq)
        #print(set(dictionary[id])) ###for checking only ACTG are present
    for key in dictionary: #loop counting the ocurrences of each nucleotide in all sequences
        As += str(dictionary[key]).count('A')
        Ts += str(dictionary[key]).count('T')
        Cs += str(dictionary[key]).count('C')
        Gs += str(dictionary[key]).count('G')
nt_counts = {'A': As, 'T': Ts, 'C': Cs, 'G': Gs} #creating the dictionary
print(f'{nt_counts}\nGC content: {(nt_counts['G']+nt_counts['C'])/tot_len:.2%}\nTotal lentgth: {tot_len}')
        #sequence_set = set(line)
        #if sequence_set 