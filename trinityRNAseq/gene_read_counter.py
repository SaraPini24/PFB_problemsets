#!/usr/bin/env python

import os, sys, re, pprint

expression_dict = {}
with open(sys.argv[1], 'r') as sam:
    for line in sam:
        print(line)
        line = line.split('\t')
        gene_name = re.sub(r'\^.+', '', line[2])
        if gene_name not in expression_dict:
            expression_dict[gene_name] = {}
            expression_dict[gene_name]['sequences'] = []
            expression_dict[gene_name]['sequences'].append(line[9])
        else:
            expression_dict[gene_name]['sequences'].append(line[9])
#print(expression_dict)
for gene in expression_dict:
    read_count = len(set(expression_dict[gene]['sequences']))
    expression_dict[gene]['counts'] = read_count

print(f'Gene\tRead_Counts')
for gene in expression_dict:
    print('{}\t{}'.format(gene, expression_dict[gene]['counts']))