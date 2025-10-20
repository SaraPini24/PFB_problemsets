#!/usr/bin/env python3

#Exercise 1

#Create a new FASTA parser that uses BioPython SeqIO (e.g. from Bio import SeqIO) (review SeqIO.parse in notes) to print the sequence name, description, and sequence as tab delimited output
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction #gc_fraction will work with Bio.SeqRecord.SeqRecord objects as well as a literal DNA sequence string(seq_record) to calculate GC content
import pprint
import sys

filename = sys.argv[1]

seq_dictionary = SeqIO.to_dict(SeqIO.parse(filename, 'fasta'))
total_seq = len(seq_dictionary)
total_nt = 0
total_gc = 0
lengthmax = 0
gc_content_max = 0
gc_content_min = 1
pprint.pprint(seq_dictionary)
for key in seq_dictionary:
    print ('%s\t%s\t%s' % (seq_dictionary[key].id, seq_dictionary[key].description, seq_dictionary[key].seq))
    total_nt = total_nt + len(seq_dictionary[key].seq)
lengthmin = total_nt
for key in seq_dictionary:
    length1 = len(seq_dictionary[key].seq)
    gc_content = gc_fraction(seq_dictionary[key])
 #   Cs = seq_dictionary[key].seq.count('C')
 #   Gs = seq_dictionary[key].seq.count('G')
 #   gc_content = (Cs + Gs)/length1
    total_gc = total_gc + gc_content
    if length1 > lengthmax:
        lengthmax = length1
    if length1 < lengthmin:
        lengthmin = length1
    if gc_content > gc_content_max:
        gc_content_max = gc_content
    if gc_content < gc_content_min:
        gc_content_min = gc_content

print(f'sequence count: {total_seq}\ntotal number of nucleotides:{total_nt}\navg len: {total_nt/total_seq:g}')
print(f'shortest len: {lengthmin}\nlongest len: {lengthmax}')
print(f'avg GC content: {total_gc/total_seq:.2%}\nlowest GC content: {gc_content_min:.2%}\nhighest GC content: {gc_content_max:.2%}')


