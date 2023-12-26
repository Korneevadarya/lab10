from itertools import product

def unique_combinations(*sequences):
    for combination in product(*sequences):
        unique_combination = (combination)
        yield unique_combination

seq1 = [0, 2]
seq2 = [0, 3]
seq3 = [0 ,4]

for combination in unique_combinations(seq1, seq2, seq3):
    print(combination)