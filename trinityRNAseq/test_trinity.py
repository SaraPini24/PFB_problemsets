import os, sys
def seq_list_from_fastq_file(fastq_filename):

    seq_list = list()

    ## begin your code
    with open(fastq_filename, 'r') as fastq:
        count = 0
        for line in fastq:
            line = line.rstrip()
            count += 1
            if count%4 == 2:
                seq_list.append(line)
    ## end your code

    return seq_list

fastq_filename = sys.argv[1]
sequence = seq_list_from_fastq_file(fastq_filename)
#print(sequence)
kmer_length = int(sys.argv[2])

def sequence_to_kmer_list(sequence, kmer_length):

    kmers_list = list()

    ## begin your code
    nt_count = 0
    for nt in sequence:
        kmer = sequence[nt_count:nt_count + kmer_length]
        nt_count += 1
        if len(kmer) == kmer_length:
            kmers_list.append(kmer)

    ## end your code

    return kmers_list

#for i in sequence:
kmer_list = sequence_to_kmer_list(sequence[0],kmer_length)

def count_kmers(kmer_list):

    kmer_count_dict = dict()

    ##################
    ## Step 2:
    ## begin your code
    for kmer in kmer_list:
        if not kmer in kmer_count_dict:
            kmer_count_dict[kmer] = 1
        else:
            kmer_count_dict[kmer] += 1
    
    ## end your code
    ################

    return kmer_count_dict
print(count_kmers(kmer_list))

all_kmers = list()
for sequence in sequence:
    kmers_list = sequence_to_kmer_list(sequence, kmer_length)
    all_kmers.extend(kmers_list)
    ## end your code
    #######################

kmer_count_dict = count_kmers(
    all_kmers
    )  # see step 2 above. You implement this. :-)

unique_kmers = list(kmer_count_dict.keys())

    #########################
    ## Step 3: sort unique_kmers by abundance descendingly
    ## (Note, you can run and test without first implementing Step 3)
    ## begin your code       hint: see the built-in 'sorted' method documentation
unique_kmers = {k: v for k,v in sorted(kmer_count_dict.items(), key=lambda item: item[1], reverse=True)}
#unique_kmers_sort = sorted(unique_kmers, reverse= True, key= kmer_count_dict[])
print(unique_kmers)
