from math import exp, log
from random import uniform

from pandas import DataFrame
import matplotlib.pyplot as plt


def calculate_pileup_probability(rate, length, gap):
    """
    Equation taken from the following paper.
    https://dx.doi.org/10.1016/j.nima.2007.05.323

    :param rate: The detector rate in counts per second
    :param length: The filter length in seconds
    :param gap: The filter gap in seconds.
    :return:
    """
    x = rate * (2 * length + gap)
    return (1 + x) * (1 - exp(-2 * x))


rate = 20000
length = 0.20e-6
gap = 0.64e-6

num_experiments = 10

theory = list()
poisson = list()
for k in range(0, num_experiments):
    count1 = 0
    count2 = 0
    num_choices = 10
    for i in range(0, num_choices):
        if uniform(0, 1) < calculate_pileup_probability(rate, length, gap):
            count1 = count1 + 1
        if -log(1. - uniform(0, 1)) / rate <= length + gap:
            count2 = count2 + 1
    theory.append(count1)
    poisson.append(count2)

ax = plt.gca()

bins = 10
DataFrame(theory).hist(bins=bins*2, range=[0, bins], ax=ax, alpha=0.5, color='black').flatten()[
    0].get_figure().show()
DataFrame(poisson).hist(bins=bins*2, range=[0, bins], ax=ax, alpha=0.5, color='red').flatten()[
    0].get_figure().show()
