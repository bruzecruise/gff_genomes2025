# gff_genomes2025

## (1) python script called split_fasta.py 

This script is used to split primary and alternate contigs after polishing with medaka and after purging duplicates with purge_dup. 

### usage
split_fasta('consensus.fasta')

The python function parses the merged fasta file based on the headers into 5 files: alternate = atg, primary = ptg, purged_primary = hap, and other = non-matches.

## (2) python script called longest_iso.faa
This script takes a .faa protein fasta file from an annotation pipeline and filters out only the longest isoform for each gene. Useful for BUSCO analysis
