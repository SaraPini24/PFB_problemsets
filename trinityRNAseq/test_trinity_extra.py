#!/usr/bin/env python

import os, sys, math

from sequence_to_kmer_list import *
from fastq_file_to_sequence_list import *

## method: get_complexity(kmer_list)
##
## Computes the complexity of each kmer using Shannon's Entropy
##
##  input parameters:
##
##  kmer_list : list of kmers (type: list)
##               ie.  ["GATC", "TCGA", "GATC", ...]
##
##
##  returns kmer_complexity_dict : dict containing ( kmer : complexity )
##                    ie.  {  "GATC" : 2,
##                            "TTTT" : 0,
##                             ...       }


def get_complexity(kmer_list):
    kmer_complexity_dict = dict()
    Entropy = 0
    for kmer in kmer_list:
        unique_nt = ['A', 'C', 'G', 'T']
        if set(kmer).issubset(unique_nt):
            for nt in unique_nt:
                p = kmer.count(nt)/len(kmer)    
                Entropy += p*math.log2(p)
            kmer_complexity_dict[kmer] = -Entropy


sys.exit(0)  # always good practice to indicate worked ok!


if __name__ == "__main__":
    main()
