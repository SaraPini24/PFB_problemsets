#!/usr/bin/env python3

#Exercise 2, 3, 4, 5, 6

import sys
import re

sequence = sys.argv[1]

#Parsing FASTA file
parsed = {}

with open(sequence, 'r') as fasta:
    for line in fasta:
        line = line.rstrip()
        if line.startswith('>'):
            for match in re.finditer(r'^(>\S+)(.+)?', line):
                name_seq = match.group(1).lstrip('>')
                parsed[name_seq] = {}
                parsed[name_seq]['sequence'] = ''

        else:
            parsed[name_seq]['sequence'] = parsed[name_seq]['sequence'] + line

with open('Python_08.codons-frame-1.nt.txt', 'w') as fo:
    for name_seq in parsed:
        codons = re.findall(r'(.{3})',parsed[name_seq]['sequence']) #Identifies codon from frame 1
        fo.write(f'seq{name_seq}-frame1-codons\n')
        for codon in codons:
            fo.write(f'{codon} ')
        fo.write('\n')


#Getting the codons from the 3 frames on fw strand
with open('Python_08.codons-frame-1_3.nt.txt', 'w') as fo:
    for name_seq in parsed:
        for n in range(3):
            codons = re.findall(r'(.{3})',parsed[name_seq]['sequence'][n:]) #Identifies codon from frame 1
            fo.write(f'seq{name_seq}-strand + frame{n+1}-codons\n')
            for codon in codons:
                fo.write(f'{codon} ')
            fo.write('\n')


#Getting the codons from the 3 frames on rv strand
#make rev compl
translation_tab = str.maketrans('ACTG', 'TGAC')
for name_seq in parsed:
    seq_rev = parsed[name_seq]['sequence'][::-1]
    seq_rev_compl = seq_rev.translate(translation_tab)
    parsed[name_seq]['revcompl']= seq_rev_compl

#get codons
with open('Python_08.codons-strand- frame-1_3.nt.txt', 'w') as fo:
    for name_seq in parsed:
        for n in range(3):
            codons = re.findall(r'(.{3})',parsed[name_seq]['revcompl'][n:]) #Identifies codon from frame 1
            fo.write(f'seq{name_seq}-strand - frame{n+1}-codons\n')
            for codon in codons:
                fo.write(f'{codon} ')
            fo.write('\n')

#gprint all six frames and add the six frames to parsed dictionary

for name_seq in parsed:
    parsed[name_seq]['codons +']={}
    parsed[name_seq]['codons -']={}

with open('Python_08.codons-6frames.nt.txt', 'w') as fo:
    for name_seq in parsed:
        for n in range(3):
            codons = re.findall(r'(.{3})',parsed[name_seq]['sequence'][n:]) #Identifies codon from frame 1
            if n not in parsed[name_seq]['codons +']:
                parsed[name_seq]['codons +'][f'frame{n+1}']={}
            parsed[name_seq]['codons +'][f'frame{n+1}']= codons
            fo.write(f'seq{name_seq}-strand + frame{n+1}-codons\n')
            for codon in codons:
                fo.write(f'{codon} ')
            fo.write('\n')
            codonsrev = re.findall(r'(.{3})',parsed[name_seq]['revcompl'][n:]) #Identifies codon from frame 1
            if n not in parsed[name_seq]['codons -']:
                parsed[name_seq]['codons -'][f'frame{-1-n}']={}
            parsed[name_seq]['codons -'][f'frame{-1-n}']= codonsrev
            fo.write(f'seq{name_seq}-strand - frame{n+1}-codons\n')
            for codonrev in codonsrev:
                fo.write(f'{codonrev} ')
            fo.write('\n')

#Translating the six frames
translation_table_aa = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}

with open('Python_08.translated.aa.txt', 'w') as fo:
    for name_Seq in parsed:
        fo.write(f'>>Sequence - {name_Seq}\n')
        for frame in parsed[name_Seq]['codons +']:
            fo.write(f'>{frame}:\n')
            for i in parsed[name_Seq]['codons +'][frame]:
                j = translation_table_aa[i]
                translation = re.sub(i,j,i) 
                fo.write(f'{translation}')
            fo.write('\n')
        for frame in parsed[name_Seq]['codons -']:
            fo.write(f'>{frame}:\n')
            for i in parsed[name_Seq]['codons -'][frame]:
                j = translation_table_aa[i]
                translation = re.sub(i,j,i) 
                fo.write(f'{translation}')
            fo.write('\n')