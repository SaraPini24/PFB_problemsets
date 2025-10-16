#!/usr/bin/env python3

#Exercise 5: FASTA parser script
fasta_parser = {} #creo il dizionario vuoto

with open('Python_06.fasta', 'r') as fasta:
    for line in fasta:
        #print(f'Step 1 {line}')
        line = line.rstrip() #tolgo eventuali spazi
        if line[0] == '>': #se la riga inizia per '>' aka se e un id
            line_key = line.lstrip('>') #il contenuto della riga diventa una key
            fasta_parser[line_key] = '' #assegno la key al dizionario
            #print(f'step 2 {line_key}')
        else: #se la riga non inizia per '>', aka e sequenza
            fasta_parser[line_key] = fasta_parser[line_key]+line #inserisco il testo nel valore del dizionario.

# As soon as id does not change, no new key is asigned and all the sequence is appended to the same dictionary value.

print(fasta_parser)