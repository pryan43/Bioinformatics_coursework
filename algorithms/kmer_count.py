"""
Counts the frequency of all possible 4-mers in a DNA sequence
using a sliding window approach.
"""

import Bio.SeqIO
import sys

if len(sys.argv[1]) < 2:
    print('Please provide file', file=sys.stderr)
    sys.exit(1)

file = sys.argv[1]

filename = open(file)
seqs = ''
for seq_file in Bio.SeqIO.parse(filename, 'fasta'):
    seqs += str(seq_file.seq)
    
filename.close()

letters = ['A', 'C', 'G', 'T']
kmer_seqs = ['']

for i in range(4):
    new_seq = []

    for seq in kmer_seqs:
        for letter in letters:
            new_seq.append(seq + letter)

    kmer_seqs = new_seq


kmer_num = {}
for seq in kmer_seqs:
    kmer_num[seq] = 0


for i in range(len(seqs) - 3):
    kmers = seqs[i:i+4]

    if kmers in kmer_num:
        kmer_num[kmers] += 1


for seq in kmer_seqs:
    print(kmer_num[seq], end = " ")

