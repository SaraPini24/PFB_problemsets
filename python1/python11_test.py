#!/usr/bin/env python3

#Exercise 1

#Defining the class and sttributes
class DNARecord(object):
    def __init__(self, gene_name, sequence, species_name):
        self.gene_name = gene_name
        self.sequence = sequence.upper()
        self.species_name = species_name

#Defining methods    
    def get_length(self):
        length = len(self.sequence)
        return(f'Sequence length: {length}')
    
    def nt_composition(self):
        A = self.sequence.count('A')
        C = self.sequence.count('C')
        T = self.sequence.count('T')
        G = self.sequence.count('G')
        return f'As: {A}, Cs: {C}, Ts: {T}, Gs: {G}'
    
    def gc_content(self):
        A = self.sequence.count('A')
        C = self.sequence.count('C')
        T = self.sequence.count('T')
        G = self.sequence.count('G')
        length = len(self.sequence)
        return f'GC content: {(C+G)/length:.2%}'
    
    def fasta_format(self):
        return f'>{self.gene_name}\n{self.sequence}'


##Out of the class definition
dna_rec_obj1 = DNARecord('ABC', 'AAAACGCGTTTTATCGATCGATCGATCGATCGATCGATCGATCGATCTCAGAGACTCTCAGAGAGGGAAATTTCCCATAGCTAGTCCATCGATCGTACATGCTACT', 'H.sapiens')
dna_rec_obj2 = DNARecord('DEF', 'CCCCAAAATTTTGGGG', 'M.musculus')

print(dna_rec_obj1.gene_name, dna_rec_obj1.sequence, dna_rec_obj1.species_name)
print(dna_rec_obj1.get_length())
print(dna_rec_obj1.gc_content())
print(dna_rec_obj1.nt_composition())
print(dna_rec_obj1.fasta_format())