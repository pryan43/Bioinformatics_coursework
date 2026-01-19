"""
Generates a consensus DNA sequence from aligned FASTA sequences
by counting nucleotide frequencies at each position.
"""

import Bio.SeqIO
import sys

if len(sys.argv[1]) < 2:
    print('Please provide file', file=sys.stderr)
    sys.exit(1)

file = sys.argv[1]

filename = open(file)
seqs = []
for seq_file in Bio.SeqIO.parse(filename, 'fasta'):
    seqs.append(''.join(seq_file.seq))
    
filename.close()

length =len(seqs[0])

matrix = {}

for seq in seqs:
    for i in range(length):
        base = seq[i]
        matrix[i, base] = matrix.get((i, base), 0) + 1

#print(matrix)

consensus = ''

for i in range(length):
    max_count = 0
    max_base = ''
    for base in 'ACGT':
        count = matrix.get((i, base), 0)
        if count > max_count:
            max_count = count
            max_base = base
    consensus += max_base

print(consensus)

for base in 'ACGT':
    print(base + ':', end=' ')
    for i in range(len(consensus)):
        count = matrix.get((i, base), 0)
        print(count, end=' ')
    print()


            


