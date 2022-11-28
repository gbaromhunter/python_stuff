from prob import *
from itertools import product, combinations

possible_numbers_lottery = list(range(1, 91))
# possible_numbers = list(range(1, 11))
sample_space = set(combinations(possible_numbers_lottery, 6))
# sample_space2 = set(product(possible_numbers, repeat=6))
print(len(sample_space))
# print(len(sample_space2))
