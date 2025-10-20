#!/usr/bin/env python3

#Exercise 1 BLAST

from Bio import SeqIO
import sys
import os
import subprocess

#Parsing protein sequence file and selecting S. paratyphi B proteins
filename = 'uniprot_sprot.fasta'
with open('uniprot_SparatyphiB.fasta.txt', 'w') as fo:
    for record in SeqIO.parse(filename, 'fasta'):
        if 'Salmonella paratyphi B' in record.description:
            fo.write(f'>{record.description}\n{record.seq}\n')

#Creating the db with S. pearatyphi proteins
db = 'uniprot_SparatyphiB.fasta.txt'
if not os.path.exists(f'{db}.phr'):
    makeblastdbcmd = f'makeblastdb -in {db} -dbtype prot -parse_seqids'
    makeblastdbcmd_run = subprocess.run(makeblastdbcmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if makeblastdbcmd_run.returncode != 0:
        print('FAILED db')
        exit(5)

#Alignment with blastp --- results in xml file
query = sys.argv[1]
blast_out = query + '.xml'
blastcmd = f'blastp -query {query} -db {db} -outfmt 5 -out {blast_out}'
blastcmd_run = subprocess.run(blastcmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if blastcmd_run.returncode != 0:
        print('FAILED blast')
        exit(2)

#parsing results from XML file
from Bio.Blast import NCBIXML

result_handle = open(blast_out)
blast_records = NCBIXML.parse(result_handle)
for blast_record in blast_records:
   query_id = blast_record.query_id
   for alignment in blast_record.alignments:
     for hsp in alignment.hsps:
        if hsp.expect < 1e-10:
           print(f'qid: {query_id} hit_id: {alignment.title} E: {hsp.expect:.3}' )
        
#results can be also in tsv fomat (7) than change parsing method