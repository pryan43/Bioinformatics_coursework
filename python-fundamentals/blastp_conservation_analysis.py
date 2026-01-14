"""
Purpose:
Run a BLASTP search and identify conserved protein alignments based
on e-value thresholds.

Concepts demonstrated:
- Automating external bioinformatics tools (BLAST)
- Parsing BLAST XML output
- Iterating over alignment results
- Interpreting e-values in a biological context

Note:
This script requires a local BLAST installation and is provided
as a representative example.
"""

# Special modules for running blast
from Bio.Blast.Applications import NcbiblastpCommandline
from xml.etree import ElementTree as ET
from Bio.Blast import NCBIXML


# Set the blast program and arguments as strings
blast_prog   = '/usr/local/bin/blastp'
blast_query = 'drosoph-ribosome.fasta'
blast_db    = 'yeast_ribosome_db'

# Build the command-line
cmdline = NcbiblastpCommandline(cmd=blast_prog,
                                query=blast_query,
                                db=blast_db,
                                outfmt=5,
                                out="results.xml")
# ...and execute.
stdout, stderr = cmdline()

lowest_evalue = 1e-5

result_handle = open("results.xml")
for blast_result in NCBIXML.parse(result_handle):
    for alignment in blast_result.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < 1e-5:
                print('****Alignment****')
                print('sequence:', alignment.title)
                print('length:', alignment.length)
                print('e value:', hsp.expect)

                if hsp.expect < lowest_evalue:
                    lowest_evalue = hsp.expect
                    most_conserved_prot = alignment.title

print('Most conserved protein:', most_conserved_prot)


