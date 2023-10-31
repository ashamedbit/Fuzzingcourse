

from typing import Any, Callable, List, Optional, Set, Tuple, Type

from matplotlib.backend_bases import LocationEvent
from generate_random_characters import fuzzer
from cgi_decode import *
from coverage import *

trials = 100

def population_coverage(population: List[str], function: Callable) \
        -> Tuple[Set[LocationEvent], List[int]]:
    cumulative_coverage: List[int] = []
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


def hundred_inputs() -> List[str]:
    population = []
    for i in range(trials):
        population.append(fuzzer())
    return population

runs = 100

# Create an array with TRIALS elements, all zero
sum_coverage = [0] * trials

for run in range(runs):
    all_coverage, coverage = population_coverage(hundred_inputs(), cgi_decode)
    assert len(coverage) == trials
    for i in range(trials):
        sum_coverage[i] += coverage[i]

average_coverage = []
for i in range(trials):
    average_coverage.append(sum_coverage[i] / runs)

import matplotlib.pyplot as plt

plt.plot(average_coverage)
plt.title('Coverage of cgi_decode() with random inputs')
plt.xlabel('# of inputs')
plt.ylabel('lines covered')
plt.show()