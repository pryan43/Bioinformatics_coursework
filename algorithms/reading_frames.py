"""
Identifies all possible protein sequences encoded by open reading frames
across six reading frames in a DNA sequence.
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

def complement(nuc):
    nucleotides = 'ACGT'
    complements = 'TGCA'
    i = nucleotides.find(nuc)
    if i >= 0:
        comp = complements[i]
    else:
        comp = nuc
    return comp

def reversecomp(seq):
    newseq = ""
    for nuc in seq:
        newseq = complement(nuc) + newseq
    return newseq

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

def protein_seq(seq):
    seq = seq.replace('T', 'U') 
    aa_seq = set()    

    for i in range(len(seq) - 2):  
        if seq[i:i+3]   == 'AUG':
            protein = 'M'
            for j in range(i + 3, len(seq) - 2, 3):  
                codon = seq[j:j+3]

                aa = None
                for amino_acid, codons in codon_table.items():
                    if codon in codons:
                        aa = amino_acid
                        break  

                if aa == 'STOP':  
                    aa_seq.add(protein)
                    break
                elif aa:
                    protein += aa

    return aa_seq

def reading_frames(seq):
    frames = []
    for i in range(3):
        frames.append(seq[i:])  
    reverse_seq = reversecomp(seq)
    for i in range(3):
        frames.append(reverse_seq[i:])  
    return frames

for seq in seqs:
    frames = reading_frames(seq)
    aas = set()

    for frame in frames:
        proteins = protein_seq(frame)
        aas.update(proteins)  

    for protein in aas:
        print(protein)



