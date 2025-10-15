#!/usr/bin/env python3

#Goal: find the starting and ending nucleotide position of an EcoRI GAATTC site in the forward strand

#Create a variable containing the sequence
import sys
dna = sys.argv[1]

#armonize the case of the characters to uppercase and select the subset
dna_allupp= dna.upper()

#Find start and end position of GAATTC sequence(s) in + strand
EcoRI_start = int(dna_allupp.find('GAATTC'))+1
EcoRI_end = EcoRI_start+5

print(f'____+Strand___\nEcoRI startPos: {EcoRI_start} - endPos: {EcoRI_end}')

##Find start and end position of GAATTC sequence(s) in - strand

translation_tab = str.maketrans('ACTG', 'TGAC')

#Make the complement
dna_rev_compl = dna_allupp[::-1].translate(translation_tab)


EcoRI_start_rev = int(dna_rev_compl.find('GAATTC'))+1
EcoRI_end_rev = EcoRI_start_rev+5

print(f'___-Strand___\nEcoRI startPos: {EcoRI_start_rev} - endPos: {EcoRI_end_rev}')