

from typing import Any, Callable, Optional, Set, Tuple, Type

from matplotlib.backend_bases import LocationEvent
from generate_random_characters import fuzzer
from cgi_decode import *
from coverage import *

trials = 100

# Given a list of input strings and functions 
# Return a list of numbers representing the cumulative no. of covered lines.
# For example if population is ["a*b", "a/b", "a-b"]
# And assuming the coverage of each of these input strings in order is [3, 4, 5],
# Then the cumulative coverage is [3, 7, 9]
def population_coverage(population: list, function: Callable) \
        -> Tuple[Set[LocationEvent], list]:
    cumulative_coverage: list = []
    all_coverage = set()

    for s in population:
        with Coverage() as cov:
            try:
                function(s)
            except:
                pass
        all_coverage |= cov.coverage()
        cumulative_coverage.append(len(all_coverage))

    return all_coverage, cumulative_coverage

# function to generate a number of inputs indicated by variable trials
def hundred_inputs() -> list:
    population = []
    for i in range(trials):
        population.append(fuzzer())
    return population

runs = 100

# Create an array with TRIALS elements, all zero
sum_coverage = [0] * trials
average_coverage = sum_coverage

# Implement logic to obtain cumulative coverage of cgi_decode over hundred random inputs
# Then repeat experiment for 100 runs and obtain average_coverage
# YOUR CODE GOES HERE
for run in range(runs):
    all_coverage, cum_coverage = population_coverage(hundred_inputs(), cgi_decode)
    assert len(cum_coverage) == trials
    for i in range(trials):
        sum_coverage[i] += cum_coverage[i]


# Find the average cumulative coverage over all runs
for i in range(trials):
    average_coverage[i] = (sum_coverage[i] / runs)

import matplotlib.pyplot as plt

plt.plot(average_coverage)
plt.title('Coverage of cgi_decode() with random inputs')
plt.xlabel('# of inputs')
plt.ylabel('lines covered')
plt.show()