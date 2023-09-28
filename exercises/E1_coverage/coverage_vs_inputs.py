

from typing import Any, Callable, List, Optional, Set, Tuple, Type

from matplotlib.backend_bases import LocationEvent
from generate_random_characters import fuzzer
from cgi_decode import *
from coverage import *

trials = 100

def hundred_inputs() -> List[str]:
    population = []
    for i in range(trials):
        population.append(fuzzer())
    return population

runs = 100

# Create an array with TRIALS elements, all zero
sum_coverage = [0] * trials
average_coverage = sum_coverage

# Implement logic to obtain coverage of cgi_decode over hundred random inputs
# Then repeat experiment for 100 runs and obtain average_coverage

import matplotlib.pyplot as plt

plt.plot(average_coverage)
plt.title('Coverage of cgi_decode() with random inputs')
plt.xlabel('# of inputs')
plt.ylabel('lines covered')
plt.show()