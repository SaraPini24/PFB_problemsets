#!/usr/bin/env python3

#Exercise 1-6

#Define the function for formatting fasta files
def format_sequence(dna,length):#function formatting whatever sequence (with or without new linws) aas with N characters per line
    count = 0
    formatted = ''
    line_tot = ''
    seq_header = ''
    with open(dna, 'r') as fasta:
        for line in fasta:
            line = line.rstrip()
            if '>' not in line:
                line_tot = line_tot + line
            else:
                seq_header = line
    for i in line_tot:
        count += 1
        if count % length == 0:
            formatted = formatted + i
            formatted = (f'{formatted}\n')
        else:
            formatted = formatted + i
    return f'{seq_header}\n{formatted}'

#Define the function for asseccing GC content
def gc_content(dna):
    g_content = dna.count('G')
    c_content = dna.count('C')
    return f'{(g_content+c_content)/len(dna):.2%}'

#Define the function for getting the rev conv
def get_rev_conv(dna):
    reversion_tab = str.maketrans('ACTG', 'TGAC')
    import re
    seq_rev = dna[::-1]
    seq_rev_compl = seq_rev.translate(reversion_tab)
    return seq_rev_compl



########Use functions#########
#Define the input variables
import sys
dna = sys.argv[1]
length = int(sys.argv[2])

#print results 1
with open('Python10_formatted.fasta.txt', 'w') as fo:
    fo.write(format_sequence(dna, length))

#print results 2
my_seq = 'CGTGCTTTCCACGACGGTGACACGCTTCCCTGGA'
print(gc_content(my_seq))

#print results 3
my_seq = 'CGTGCTTTCCACGACGGTGACACGCTTCCCTGGA'
print(get_rev_conv(my_seq))