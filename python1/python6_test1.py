#!/usr/bin/env python3

#Exercise 3

translation_tab = str.maketrans('ACTG', 'TGAC')

with open('Python_06.seq.txt', 'r') as my_seq: #open the sequence file
    for line in my_seq:                        #for each line of the file
        line_split = line.rstrip().split('\t') #removes \n at the end of the line and create a list splitting based on \t
        line_rev = str(line_split[1])[::-1]#transforms the sequence (index 1) in a string and returns the reverse
        line_rev = line_rev.upper() #changes the case to uppercase
        line_rev_compl = line_rev.translate(translation_tab) #creates the complement
        #print(f'{line_split[1]}\n{line_rev}\n{line_rev_compl}')
        print(f'>{line_split[0]}_revcompl\t{line_rev_compl}\n')