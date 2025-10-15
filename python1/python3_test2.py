#!/usr/bin/env python3

#create a variable that stores the DNA sequence
import sys
dna = sys.argv[1]
start_pos = int(sys.argv[2])-1
end_pos = int(sys.argv[3])

#armonize the case of the characters to uppercase and select the subset
dna_allupp= dna.upper()
dna_allupp_subset = dna_allupp[start_pos:end_pos]

#count As, Cs, Ts and Gs
n_As = dna_allupp_subset.count('A')
n_Ts = dna_allupp_subset.count('T')
n_Cs = dna_allupp_subset.count('C')
n_Gs = dna_allupp_subset.count('G')

#assess GC and AT content and print the results
dna_length = len(dna_allupp_subset)
print(f'--Sequence--\n{dna_allupp}\n--Subset--\nStart: {start_pos}\nEnd: {end_pos}\nSequence: {dna_allupp_subset}\n--Content type--\nGC content: {(n_Gs+n_Cs)/dna_length:.2%}\nAT content: {(n_As+n_Ts)/dna_length:.2%}')
