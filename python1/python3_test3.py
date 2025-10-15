#!/usr/bin/env python3

#Goal: to generate and print the reverse complement of a nucleotide sequence
#create a variable that stores the DNA sequence
import sys
dna = sys.argv[1]

#armonize the case of the characters to uppercase and select the subset
dna_allupp= dna.upper()

#reverse the sequence
dna_rev = dna_allupp[::-1]

#Create a translation table
translation_tab = str.maketrans('ACTG', 'TGAC')

#Make the complement
dna_rev_compl = dna_rev.translate(translation_tab)

print(dna_rev_compl)


####Same but mantaining the original capitalzation####

#reverse the sequence
dna_rev1 = dna[::-1]

#Create a translation table
translation_tab = str.maketrans('ACTG', 'TGAC')
translation_tab1 = str.maketrans('actg', 'tgac')

#Make the complement
dna_rev_compl1 = dna_rev1.translate(translation_tab).translate(translation_tab1)

print(dna_rev_compl1)
