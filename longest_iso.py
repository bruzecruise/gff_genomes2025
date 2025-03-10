#!/bin/python
#### get longest isoform faa protien fasta file for ncbi EGAPx output
# input needs to be names complete.protiens.faa
from Bio import SeqIO
from collections import defaultdict
import re

# Load the FASTA file
input_fasta = 'complete.proteins.faa'
output_fasta = 'longest_isoforms.faa'

# Dictionary to hold the longest isoform for each gene
longest_isoforms = {}

# Parse the input FASTA file
with open(input_fasta, 'r') as fasta_file:
    for record in SeqIO.parse(fasta_file, 'fasta'):
        # Extract the gene ID using regular expressions
        match = re.search(r'gnl\|WGS:ZZZZ\|([A-Z0-9_]+)-P\d+ ', record.description)
        if match:
            gene_id = match.group(1)
            isoform_length = len(record.seq)
            
            # If this gene is not in the dictionary or this isoform is longer, update the dictionary
            if gene_id not in longest_isoforms or isoform_length > len(longest_isoforms[gene_id].seq):
                longest_isoforms[gene_id] = record

# Write the longest isoforms to the output FASTA file
with open(output_fasta, 'w') as fasta_out:
    SeqIO.write(longest_isoforms.values(), fasta_out, 'fasta')

print(f"Longest isoforms have been written to {output_fasta}")
