def split_fasta(input_file):
    # Define the output file names
    atg_file = 'atg_sequences.fasta'
    ptg_file = 'ptg_sequences.fasta'  
    hap_file = 'hap_sequences.fasta'
    mito_file = 'mito_sequences.fasta'
    other_file = 'other_sequences.fasta'

    with open(input_file, 'r') as infile, \
         open(atg_file, 'w') as atg_outfile, \
         open(ptg_file, 'w') as ptg_outfile, \
         open(hap_file, 'w') as hap_outfile, \
         open(mito_file, 'w') as mito_outfile, \
         open(other_file, 'w') as other_outfile:
        
        current_header = None
        current_sequence = []

        for line in infile:
            line = line.strip()
            if line.startswith(">"):  # Header line
                # Write the previous sequence to the appropriate file
                if current_header:
                    output_file = get_output_file(current_header, atg_outfile, ptg_outfile, hap_outfile, mito_outfile, other_outfile)
                    output_file.write(current_header + '\n' + ''.join(current_sequence) + '\n')
                
                # Start a new sequence
                current_header = line
                current_sequence = []
            else:  # Sequence line
                current_sequence.append(line)

        # Write the last sequence
        if current_header:
            output_file = get_output_file(current_header, atg_outfile, ptg_outfile, hap_outfile, mito_outfile, other_outfile)
            output_file.write(current_header + '\n' + ''.join(current_sequence) + '\n')

    print(f"Sequences have been split into {atg_file}, {ptg_file}, {hap_file}, {mito_file}, and {other_file}")

def get_output_file(header, atg_outfile, ptg_outfile, hap_outfile, mito_outfile, other_outfile):
    if header.startswith(">atg"):
        return atg_outfile
    elif header.startswith(">ptg"):  # Changed from pth to ptg
        return ptg_outfile
    elif header.startswith(">hap"):
        return hap_outfile
    elif header.startswith(">MITO"):
        return mito_outfile
    else:
        return other_outfile
