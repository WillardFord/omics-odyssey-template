# Implementing with BioPython

import sys
from Bio.Align import substitution_matrices
from Bio import Align

user_mode = "local"
user_match_score = 1.0
user_mismatch_score = -1.0
user_gap_score = -2.5
user_sub_matrix_name = "BLOSUM62"

user_substitution_matrix = substitution_matrices.load(user_sub_matrix_name)

target = "LAPRHKDEMETQCG"
query = "LAPRHKDEMETQCG"

aligner = Align.PairwiseAligner(mode=user_mode, match_score=user_match_score, mismatch_score=user_mismatch_score, gap_score=user_gap_score)

score = aligner.score(target, query)

print(score)
