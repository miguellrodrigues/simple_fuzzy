from fuzzy_set import FuzzySet, de_fuzzy

money = 35
people = 60

low_money = FuzzySet(FuzzySet.TRAPEZOIDAL, [0, 5, 25, 65])
medium_money = FuzzySet(FuzzySet.TRIANGULAR, [25, 65, 95])
high_money = FuzzySet(FuzzySet.TRIANGULAR, [40, 50, 70, 80])

low_people = FuzzySet(FuzzySet.TRAPEZOIDAL, [0, 10, 25, 69])
high_people = FuzzySet(FuzzySet.TRAPEZOIDAL, [20, 40, 55, 80])

low_output = FuzzySet(FuzzySet.TRAPEZOIDAL, [10, 20, 30, 40])
medium_output = FuzzySet(FuzzySet.TRIANGULAR, [50, 60, 70])
high_output = FuzzySet(FuzzySet.TRAPEZOIDAL, [80, 90, 100, 120])

# if money is high or people is low then output is low
# if money is medium and people is high then output is medium
# if money is low then output is high

rules = [
    max(high_money.calculate_pertinence(money), low_people.calculate_pertinence(people)),
    min(medium_money.calculate_pertinence(money), high_people.calculate_pertinence(people)),
    low_money.calculate_pertinence(money)
]

output = de_fuzzy([low_output.values, medium_output.values, high_output.values], [rules[0], rules[1], rules[2]])

print(output)
