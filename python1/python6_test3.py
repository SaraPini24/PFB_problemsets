#!/usr/bin/env python3

#Exercise 5: enerate gene lists and then compare the gene lists

########!!!!!!!shuld be ok BUT shuld be teted on control data!!!!!!!###########


all_set = set()
pigmentation_set = set()
proliferation_set = set()
tf_set = set()

with open('ferret_all_genes.tsv', 'r') as all_genes, open('ferret_pigmentation_genes.tsv', 'r') as pigmentation, open('ferret_stemcellproliferation_genes.tsv', 'r') as proliferation, open('ferret_transcriptionFactors.tsv', 'r') as tf:
    for line in all_genes: #one for loop for file modifying the gene list into a set
        if 'Gene stable ID' not in line:
            line = line.rstrip()
            all_set.add(line)
    for line in pigmentation:
        if 'Gene stable ID' not in line:
            line = line.rstrip()
            pigmentation_set.add(line)
    for line in proliferation:
        if 'Gene stable ID' not in line:
            line = line.rstrip()
            proliferation_set.add(line)
    for line in tf:
        if 'Gene stable ID' not in line:
            line = line.rstrip()
            tf_set.add(line)

non_proliferation_set = all_set - proliferation_set
pigment_prolif_set = proliferation_set & pigmentation_set
tf_prolif_set = proliferation_set & tf_set
#print(tf_prolif_set)