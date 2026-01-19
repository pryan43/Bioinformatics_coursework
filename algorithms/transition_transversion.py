"""
Calculates the transition-to-transversion mutation ratio
between two aligned DNA sequences.
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
    
seq1 = seqs[0]
seq2 = seqs[1]


filename.close()


def ratio(seq1, seq2):
    transitions = 0
    transversions = 0

    possible_trans = [('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')]

    for i in range(len(seq1)):
        nuc1 = seq1[i]
        nuc2 = seq2[i]

        if nuc1 != nuc2:  
            if (nuc1, nuc2) in possible_trans:
                transitions += 1
            else:
                transversions += 1

    return transitions / transversions

print(round(ratio(seq1, seq2), 11))
