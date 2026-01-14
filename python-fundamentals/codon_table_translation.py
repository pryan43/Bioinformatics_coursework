"""
Purpose:
Parse a codon table file and determine whether a nucleotide sequence
begins with a valid translation start codon.

Concepts demonstrated:
- Dictionary construction
- Working with biological reference tables
- Command-line arguments
"""
import sys

codon_table_file = sys.argv[1]
nucleotide_seq = sys.argv[2]

f = open(codon_table_file)
data = {}
for l in f:
    sl = l.split()
    key = sl[0]
    value = sl[2]
    data[key] = value    
f.close()

b1 = data['Base1']
b2 = data['Base2']
b3 = data['Base3']
aa = data['AAs']
st = data['Starts']

codons = {}
init = {}
n = len(aa)
for i in range(n):
    codon = b1[i] + b2[i] + b3[i]
    codons[codon] = aa[i]
    init[codon] = (st[i] == 'M')

f = open(nucleotide_seq)
seq = ''.join(f.read().split())
f.close()
seqlen = len(seq)
aaseq = []
for i in range(0,seqlen,3):
    codon = seq[i:i+3]
    aa = codons[codon]
    aaseq.append(aa)
aa_seq =''.join(aaseq)

initial_codon = seq[:3]
correct_start = init.get(initial_codon, False)

print('Is the initial codon a valid translation start site?:', correct_start)

