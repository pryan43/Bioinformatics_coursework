"""
Removes introns from a DNA sequence, transcribes the remaining exons,
and translates the resulting RNA into a protein sequence.
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

seq = seqs[0]
introns = seqs[1:]

    
codon_table = {
    'F':['UUU', 'UUC'], 'L':['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
    'I':['AUU', 'AUC', 'AUA'], 'M': 'AUG', 'V':['GUU', 'GUC', 'GUA', 'GUG'],
    'S':['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'], 'P':['CCU', 'CCC', 'CCA', 'CCG'],
    'T':['ACU', 'ACC', 'ACA', 'ACG'], 'A':['GCU', 'GCC', 'GCA', 'GCG'],
    'Y':['UAU', 'UAC'], 'STOP':['UAA', 'UAG', 'UGA'], 'H':['CAU', 'CAC'],
    'Q':['CAA', 'CAG'], 'N':['AAU', 'AAC'], 'K':['AAA', 'AAG'],
    'D':['GAU', 'GAC'], 'E':['GAA', 'GAG'], 'C':['UGU', 'UGC'],
    'W':'UGG', 'R':['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'G':['GGU', 'GGC', 'GGA', 'GGG']}

def transcription(seq):
    return seq.replace('T', 'U')


def protein_seq(seq):
    aa_seq = ''

    for i in range(0, len(seq), 3):
        codon = seq[i:i+3]

        for aa, codons in codon_table.items():
            if codon in codons:
                if aa == 'STOP':
                    return aa_seq
                aa_seq += aa
    return aa_seq

def no_introns(seq, introns):
    for i in introns:
        seq = seq.replace(i, '')
    return seq


exons_only = no_introns(seq, introns)

protein = protein_seq(transcription(exons_only))


print(protein)
