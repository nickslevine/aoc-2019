from utils import read_input, print_answers
from math import floor

lines = read_input('01.txt')


def calc_fuel(x):
    return floor(int(x)/3) - 2


# Part 1
result_01 = sum(map(calc_fuel, lines))

# Part 2
result_02 = 0
for n in lines:
    n = int(n)
    while n > 0:
        n = calc_fuel(n)
        if n > 0:
            result_02 += n

# Results
print_answers(result_01, result_02)
