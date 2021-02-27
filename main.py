from matplotlib.ticker import ScalarFormatter

from fuzzy_set import FuzzySet
import matplotlib.pyplot as plt

low_values = FuzzySet(FuzzySet.TRAPEZOIDAL, [0, 5, 35, 60])
medium_values = FuzzySet(FuzzySet.TRIANGULAR, [40, 60, 80])
high_values = FuzzySet(FuzzySet.TRAPEZOIDAL, [60, 85, 100, 120])

sets = [low_values, medium_values, high_values]

values = [[], [], []]
pertinence_set = [[], [], []]

print(" ")

for i in range(len(sets)):
    for value in range(120):
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

print(low_values.calculate_pertinence(30))
print(medium_values.calculate_pertinence(30))
print(high_values.calculate_pertinence(30))