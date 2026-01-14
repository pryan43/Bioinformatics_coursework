"""
Purpose:
Compare amino acid frequency distributions between protein sequences
parsed from FASTA and SwissProt XML files.

Concepts demonstrated:
- Use of Biopython for sequence parsing
- Handling compressed (.gz) files
- Dictionary-based frequency calculations
- Comparison of biological datasets
"""

import Bio.SeqIO
import sys
import gzip
import os

# Check the input
if len(sys.argv) < 3:
    print("Please provide a sequence file", file=sys.stderr)
    sys.exit(1)

# FOR part 1a fasta
seqfilename_xml = sys.argv[1]

homedir = '/home/student'

downloads_dir = os.path.join(homedir, 'Downloads')

filename_xml = os.path.join(downloads_dir, seqfilename_xml)

if os.path.exists(filename_xml):
    print(filename_xml, "is there")
else:
    print(filename_xml, "does not exist")


if filename_xml.endswith('.gz'):
    seqfile = gzip.open(filename_xml, 'rt')
else:
    seqfile = open(filename_xml)
    
for record in Bio.SeqIO.parse(seqfile, "fasta"):
    break
seqfile.close()


#part 1b XML
seqfilename_swiss = sys.argv[2]


filename_swiss = os.path.join(downloads_dir, seqfilename_swiss)

if os.path.exists(filename_swiss):
    print(filename_swiss, "is there")
else:
    print(filename_swiss, "does not exist")

if filename_swiss.endswith('.gz'):
    file = gzip.open(filename_swiss, 'rt')
else:
    file = open(filename_swiss)
    
for seq_record in Bio.SeqIO.parse(file, "uniprot-xml"):
    break
seqfile.close()

#defining functions

total_aa_fasta = len(record)


total_aa_xml = len(seq_record)


def aa_count(seq):
    counts = {}
    for aa in seq:
        if aa in counts:
            counts[aa] += 1
        else:
            counts[aa] = 1
    return counts
          

def aa_freq(counts, total):
    freq = {}
    for aa in counts:
        freq[aa] = (counts[aa] / total) * 100
    return freq


def freq(aa_freq):
    most_freq = max(aa_freq, key=aa_freq.get)
    least_freq = min(aa_freq, key=aa_freq.get)

    return most_freq, aa_freq[most_freq], least_freq, aa_freq[least_freq]


freq_aa_fasta = aa_freq(aa_count(record), total_aa_fasta)


print("RefSeq amino-acids that occur the most and least, respectively:", freq(freq_aa_fasta))
    

freq_aa_xml = aa_freq(aa_count(seq_record), total_aa_xml)


print("SwissProt amino-acids that occur the most and least, respectively:", freq(freq_aa_xml))

#part 1c difference in freq

def diff_dicts(dict1, dict2):
    result = {}
    max_diff = 0

    for key in dict1:
        if key in dict2:
            result[key] = dict1[key] - dict2[key]
        else:
            result[key] = dict1[key]

    for key in dict2:
        if key not in dict1:
            result[key] = -dict2[key]

    for key, value in result.items():
        if abs(value) > abs(max_diff):
            max_diff = value
            biggest_diff = key

    return biggest_diff, max_diff

#xml_count = aa_count(seq_record)

#fasta_count = aa_count(record)

#print(xml_count)
#print(fasta_count)

result = diff_dicts(freq_aa_fasta, freq_aa_xml)

print('Biggest difference in frequency:', result)





