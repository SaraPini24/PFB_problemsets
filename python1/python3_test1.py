#!/usr/bin/env python3

#create a variable that stores the DNA sequence
#armonize the case of the characters to uppercase
#replace Ts with Us and save the resulting dr=equence in a new object

import sys
dna = sys.argv[1]

dna_allupp = dna.upper()
rna = dna_allupp.replace('T', 'U')
print(rna)