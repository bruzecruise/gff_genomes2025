from Bio import SeqIO

# Define file paths
## change input for your filename!!!!!!!
gbff_file_path = "GCF_014805625.2_Yale_Gfus_2_genomic.gbff"

# Dictionary to store the longest isoform for each gene
longest_isoforms = {}

# Step 1: Parse the GenBank file to extract genes and their isoforms
with open(gbff_file_path, "r") as gbff_file:
    for record in SeqIO.parse(gbff_file, "genbank"):
        for feature in record.features:
            if feature.type == "CDS":
                gene_id = feature.qualifiers.get("gene", ["unknown_gene"])[0]
                protein_id = feature.qualifiers.get("protein_id", [None])[0]
                translation = feature.qualifiers.get("translation", [""])[0]

                if gene_id and protein_id and translation:
                    if gene_id not in longest_isoforms or len(translation) > len(longest_isoforms[gene_id]["sequence"]):
                        longest_isoforms[gene_id] = {
                            "id": protein_id,
                            "sequence": translation
                        }

# Step 2: Write the longest isoforms to a new FASTA file
with open("longest_isoforms.faa", "w") as output_file:
    for gene_id, data in longest_isoforms.items():
        output_file.write(f">{data['id']} {gene_id}\n")
        sequence = data["sequence"]
        for i in range(0, len(sequence), 60):
            output_file.write(sequence[i:i+60] + "\n")

print("Longest isoforms have been written to longest_isoforms.faa")
