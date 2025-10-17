#!/usr/bin/env python3

#Exercise 5 - FASTA PARSER
import re
parsed = {}
with open('Python_07.fasta.txt', 'r') as fastq_seq:
    for line in fastq_seq:
        line = line.rstrip()
        #print(f'Step1 {line}')
        if line.startswith('>'):
            for match in re.finditer(r'^(>\S+)(.+)', line):
                print(match)
                key = match.group(1).lstrip('>')
                parsed[key] = ''
        else:
            print(f'step 2 {line}')
            parsed[key] = parsed[key] + line
print(parsed)