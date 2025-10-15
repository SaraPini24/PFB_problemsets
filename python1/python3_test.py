#!/usr/bin/env python3

#create a variable that stores the DNA sequence
#armonize the case of the characters to uppercase
#count As, Cs, Ts and Gs
#include the counts in a dictionary object
#print the dictionary

import sys
dna = sys.argv[1]

dna_allupp = dna.upper()
n_As = dna_allupp.count('A')
n_Ts = dna_allupp.count('T')
n_Cs = dna_allupp.count('C')
n_Gs = dna_allupp.count('G')

#base_counts = {'A': n_As, 'T': n_Ts, 'C': n_Cs, 'G': n_Gs}
print(f'--Sequence--\n{dna_allupp}\n--Nucleotide counts--\nA: {n_As}\nT: {n_Ts}\nC: {n_Cs}\nG: {n_Gs}')

#assess GC and AT content
dna_length = len(dna_allupp)
print(f'--Content type--\nGC content: {(n_Gs+n_Cs)/dna_length:.2%}\nAT content: {(n_As+n_Ts)/dna_length:.2%}')
