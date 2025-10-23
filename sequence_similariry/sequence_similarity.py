#!/usr/bin/env python

import sys

filetype = sys.argv[1] #File with single sequence blast (rand5 (1 sequence) or randall(10 sequences))
seq_length = int(sys.argv[2]) #Length of the sequences to be compared (200 or 800)

query = str() 
matrices = ['PAM70', 'PAM30', 'BLOSUM80', 'BLOSUM62']
blast_dict = {}

for mat in matrices:
    filename = f'blast_{filetype}-{seq_length}_v_qfo_{mat}.txt'
    blast_dict[mat] = {}
    with open(filename, 'r') as file:
        for line in file:
            if 'Query' in line:
                newline = line.split(' ')
                query = newline[2]
                if query not in blast_dict[mat]:
                    blast_dict[mat][query] = {}
            
            for query in blast_dict[mat]:
                if query in line and 'Query' not in line:
                    newline = line.split('\t')
                    subject = newline[1]
                    blast_dict[mat][query][subject] = {}
                    identity = newline[2]
                    blast_dict[mat][query][subject]['Identity'] = identity
                    alignlength = newline[3]
                    blast_dict[mat][query][subject]['Alignment length'] = alignlength
                    e_value = newline[10]
                    blast_dict[mat][query][subject]['E value'] = e_value
                    #print(mat, query, identity, alignlength, e_value)

print(f'####Summary table of BLAST search result for set {filetype}-{seq_length}####')
print('==============================================================================')
print(f'Matrix\t%Identity\tAlignmentLength\tEvalue\tQueryID')
evaluelist = list()
for mat in matrices:
    for query in blast_dict[mat]:
        for subject in blast_dict[mat][query]:
            evaluelist.append(blast_dict[mat][query][subject]['E value'])
        e_val_top = max(evaluelist)
        for subject in blast_dict[mat][query]:
            if e_val_top in blast_dict[mat][query][subject]['E value']:
                identitytop = blast_dict[mat][query][subject]['Identity']
                alignlengthtop = blast_dict[mat][query][subject]['Alignment length']
    print(f'{mat}\t{identitytop}\t{alignlengthtop}\t{e_val_top}\t{query}')