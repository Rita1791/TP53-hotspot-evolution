from Bio import AlignIO
import numpy as np

alignment = AlignIO.read("data/processed/TP53_MSA.fasta", "fasta")

def conservation_score(column):
    counts = {}
    for aa in column:
        if aa != "-":
            counts[aa] = counts.get(aa, 0) + 1
    return max(counts.values()) / sum(counts.values())

scores = []
for i in range(alignment.get_alignment_length()):
    column = alignment[:, i]
    scores.append(conservation_score(column))

print("Computed conservation scores")
