#!/usr/bin/env python3

#create a variable that stores the DNA sequence

import sys
dna = sys.argv[1]

#armonize the case of the characters to uppercase
dna_allupp = dna.upper()
#count As, Cs, Ts and Gs
n_As = dna_allupp.count('A')
n_Ts = dna_allupp.count('T')
n_Cs = dna_allupp.count('C')
n_Gs = dna_allupp.count('G')

#base_counts = {'A': n_As, 'T': n_Ts, 'C': n_Cs, 'G': n_Gs}
print(f'--Sequence--\n{dna_allupp}\n--Nucleotide counts--\nA: {n_As}\nT: {n_Ts}\nC: {n_Cs}\nG: {n_Gs}')

#assess GC and AT content
dna_length = len(dna_allupp)
print(f'--Content type--\nGC content: {(n_Gs+n_Cs)/dna_length:.2%}\nAT content: {(n_As+n_Ts)/dna_length:.2%}')
