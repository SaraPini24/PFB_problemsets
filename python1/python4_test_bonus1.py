#!/usr/bin/env python3

###BONUS EXERCISE.2###

dictionary={}
with open("result.fasta_aln.txt") as my_seq: #Results of sequence alignment from Python_04.fasta.txt
    for line in my_seq:
        line =line.rstrip()
        if '>' in line:
            line_key=line.lstrip(">")
            dictionary[line_key]=''
        else:
            dictionary[line_key]=dictionary[line_key]+line


#for i in range(0,lungheza valori dizionario)):
    
#print(dictionary)