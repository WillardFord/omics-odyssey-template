# Implementing with BioPython

from Bio.Align import substitution_matrices
from Bio import Align


def align(target, query, sub_matrix_name="BLOSUM62"):

    sub_matrix = substitution_matrices.load(sub_matrix_name)
    aligner = Align.PairwiseAligner(mode="local", substitution_matrix=sub_matrix)

    alignments = aligner.align(target, query)

    top_alignment = alignments[0]
    top_score = top_alignment.score

    return (top_score, top_alignment) # returns top score and top alignment object (needs to be printed to be visualised)