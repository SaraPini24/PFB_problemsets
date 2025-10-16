#!/usr/bin/env python3

###BONUS EXERCISE.1###

#Sometimes you may need to show that some element or pattern in your DNA sequence is significant and not present by chance. One way to do this is to create 10s of thousands of shuffled sequences and see how many times you find your pattern.

#Create a shuffled sequence
import random #module in python generating randomness
import sys
seq_str = sys.argv[1] #provide a starting sequence
seq_list = list(seq_str) #change the str into list so that each letter of the original sequence gains an index

for i in range(len(seq_list)): #for each letter of the sequence
    j = random.randrange(len(seq_list)) #selects a random position in the range of the lyst (0, length-1)
    a = random.randrange(len(seq_list)) #selects a random position in the range of the lyst (0, length-1)
    seq_list[a], seq_list[j] = seq_list[j], seq_list[a] #swops the letters at the two positions
    print(''.join(seq_list)) #prints all the sequences