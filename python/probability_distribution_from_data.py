from pandas import DataFrame
import matplotlib.pyplot as plt
from numpy import random

from sample_spectrum import cs137_spectrum

root_binning_factor = 2

choices = [x[0] / root_binning_factor for x in cs137_spectrum]
counts = [x[1] for x in cs137_spectrum]
weights = [x / sum(counts) for x in counts]

num_choices = 2563370
bins = 750

ax = plt.gca()
DataFrame(random.choice(choices, num_choices, p=weights)).hist(bins=bins * root_binning_factor,
                                                               range=[0, bins], ax=ax).flatten()[
    0].get_figure().show()
