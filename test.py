from fuzzy_set import FuzzySet, de_fuzzy

temperature = 35
humidity = 30

low_temp = FuzzySet(FuzzySet.SINUSOIDAL, [.03, 7.5])
ideal_temp = FuzzySet(FuzzySet.SINUSOIDAL, [.03, 22.5])
high_temp = FuzzySet(FuzzySet.SINUSOIDAL, [.03, 37.5])

low_humidity = FuzzySet(FuzzySet.SINUSOIDAL, [.0005, 0])
ideal_humidity = FuzzySet(FuzzySet.SINUSOIDAL, [.005, 60])
high_humidity = FuzzySet(FuzzySet.SINUSOIDAL, [.0012, 100])

low_output = FuzzySet(FuzzySet.SINUSOIDAL, [.0001, 0])
medium_output = FuzzySet(FuzzySet.SINUSOIDAL, [.0001, 250])
high_output = FuzzySet(FuzzySet.SINUSOIDAL, [.0001, 500])

# 1. if temperature is low and humidity is low then volume is medium
# 2. if temperature is low and humidity is ideal then volume is low
# 3. if temperature is low and humidity is high then volume is low
# 4. if temperature is ideal and humidity is low then volume is medium
# 5. if temperature is ideal and humidity is ideal then volume is medium
# 6. if temperature is ideal and humidity is high then volume is low
# 7. if temperature is high and humidity is low then volume is high
# 8. if temperature is high and humidity is ideal then volume is high
# 9. if temperature is high and humidity is high then volume is medium

low_temp_pertinence = low_temp.calculate_pertinence(temperature)
ideal_temp_pertinence = ideal_temp.calculate_pertinence(temperature)
high_temp_pertinence = high_temp.calculate_pertinence(temperature)

low_humidity_pertinence = low_humidity.calculate_pertinence(humidity)
ideal_humidity_pertinence = ideal_humidity.calculate_pertinence(humidity)
high_humidity_pertinence = high_humidity.calculate_pertinence(humidity)

rules = [
    min(low_temp_pertinence, low_humidity_pertinence),
    min(low_temp_pertinence, ideal_humidity_pertinence),
    min(low_temp_pertinence, high_humidity_pertinence),

    min(ideal_temp_pertinence, low_humidity_pertinence),
    min(ideal_temp_pertinence, ideal_humidity_pertinence),
    min(ideal_temp_pertinence, high_humidity_pertinence),

    min(high_temp_pertinence, low_humidity_pertinence),
    min(high_temp_pertinence, ideal_humidity_pertinence),
    min(high_temp_pertinence, high_humidity_pertinence),
]

p = max(rules)

print(rules)
print(" ")
print(p)
print(" ")

volume = ''

if p == rules[0]:
    volume = 'medium'
elif p == rules[1]:
    volume = 'low'
elif p == rules[2]:
    volume = 'low'
elif p == rules[3]:
    volume = 'medium'
elif p == rules[4]:
    volume = 'medium'
elif p == rules[5]:
    volume = 'low'
elif p == rules[6]:
    volume = 'high'
elif p == rules[7]:
    volume = 'high'
elif p == rules[8]:
    volume = 'medium'

print(volume)

if volume == 'low':
    print(de_fuzzy([.0, 125], p))
elif volume == 'medium':
    print(de_fuzzy([125, 375], p))
elif volume == 'high':
    print(de_fuzzy([375, 500], p))
