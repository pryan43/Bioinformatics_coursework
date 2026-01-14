"""
Purpose:
Perform basic DNA sequence transformations, including reverse,
complement, and reverse complement, based on a user-specified command.

Concepts demonstrated:
- String manipulation
- Functions and modular code
- Command-line arguments
"""
import sys

file = sys.argv[1]
command = sys.argv[2]

input_seq = ''.join(open(file).read().split())

def complement(nuc):
    nuc = nuc.upper()
    nucleotides = 'ACGT'
    complements = 'TGCA'
    i = nucleotides.find(nuc)
    if i >= 0:
        comp = complements[i]
    else:
        comp = nuc
    return comp

def reverse_seq(seq):
    seq = seq.upper()
    r_seq = ""
    for nuc in seq:
        r_seq = nuc + r_seq
    return r_seq

def reversecomp(seq):
    seq = seq.upper()
    newseq = ""
    for nuc in seq:
        newseq = complement(nuc) + newseq
    return newseq
    

if command == 'Complement':
    print(input_seq, reversecomp(reverse_seq(input_seq)))
elif command == 'Reverse':
    print(input_seq, reverse_seq(input_seq))
elif command == 'ReverseComplement':
    print(input_seq, reversecomp(input_seq))
else:
    print('Error: incorrect command')









