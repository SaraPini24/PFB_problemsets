#!/usr/bin/env python3

#Exercise 13

#create a list
seq_list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

#Print the position and length of each sequence
for seq in seq_list:
    print(f'{seq_list.index(seq)}\t{len(seq)}\t{seq}')

#Sort sequences longest to shortest
seq_list_sorted = sorted(seq_list, key=len, reverse=True)
for i in seq_list_sorted:
    print(i)
