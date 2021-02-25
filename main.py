from matplotlib.ticker import ScalarFormatter

from fuzzy_set import FuzzySet
import matplotlib.pyplot as plt

low_values = FuzzySet(FuzzySet.SINUSOIDAL, [.0001, 0])
medium_values = FuzzySet(FuzzySet.SINUSOIDAL, [.0001, 250])
high_values = FuzzySet(FuzzySet.SINUSOIDAL, [.0001, 500])

sets = [low_values, medium_values, high_values]

values = [[], [], []]
pertinence_set = [[], [], []]

print(" ")

for i in range(len(sets)):
    for value in range(501):
        values[i].append(value)

        pertinence_set[i].append(sets[i].calculate_pertinence(value))

fig, axis = plt.subplots()

formatter = ScalarFormatter()
formatter.set_scientific(False)

for i in range(len(sets)):
    axis.plot(values[i], pertinence_set[i])
    for ax in [axis.xaxis, axis.yaxis]:
        ax.set_major_formatter(formatter)

plt.show()

print(medium_values.calculate_pertinence(125))