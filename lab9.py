from itertools import product

def unique_combinations(*sequences):
    for combination in product(*sequences):
        unique_combination = (combination)
        yield unique_combination

