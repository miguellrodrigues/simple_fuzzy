from matplotlib.ticker import ScalarFormatter

from fuzzy_set import FuzzySet
import matplotlib.pyplot as plt

low_values = FuzzySet(FuzzySet.TRIANGULAR, [0, 15, 30])
medium_values = FuzzySet(FuzzySet.TRIANGULAR, [15, 30, 45])
high_values = FuzzySet(FuzzySet.TRIANGULAR, [30, 45, 60])

sets = [low_values, medium_values, high_values]

values = [[], [], []]
pertinence_set = [[], [], []]

print(" ")

for i in range(len(sets)):
    for value in range(61):
        values[i].append(value)

        pertinence_set[i].append(sets[i].calculate_pertinence(value))

fig, axis = plt.subplots()

formatter = ScalarFormatter()
formatter.set_scientific(False)

for i in range(len(values)):
    axis.plot(values[i], pertinence_set[i])
    for ax in [axis.xaxis, axis.yaxis]:
        ax.set_major_formatter(formatter)

plt.show()
