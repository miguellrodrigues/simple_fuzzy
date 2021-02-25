from fuzzy_set import FuzzySet

temperature = 8
humidity = 57

low_temp = FuzzySet(FuzzySet.SINUSOIDAL, [.02, 7.5])
ideal_temp = FuzzySet(FuzzySet.SINUSOIDAL, [.02, 22.5])
high_temp = FuzzySet(FuzzySet.SINUSOIDAL, [.02, 37.5])


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

temp_pertinences = [
    low_temp.calculate_pertinence(temperature),
    ideal_temp.calculate_pertinence(temperature),
    high_output.calculate_pertinence(temperature)
]

temp_pertinence = max(temp_pertinences)

humidity_pertinences = [
    low_humidity.calculate_pertinence(humidity),
    ideal_humidity.calculate_pertinence(humidity),
    high_humidity.calculate_pertinence(humidity)
]

humidity_pertinence = max(humidity_pertinences)

temp = ''
hum = ''
volume = ''

if temp_pertinence == temp_pertinences[0]:
    temp = 'low'
    pass
elif temp_pertinence == temp_pertinences[1]:
    temp = 'ideal'
    pass
elif temp_pertinence == temp_pertinences[2]:
    temp = 'high'
    pass

if humidity_pertinence == humidity_pertinences[0]:
    hum = 'low'
    pass
elif humidity_pertinence == humidity_pertinences[1]:
    hum = 'ideal'
    pass
elif humidity_pertinence == humidity_pertinences[2]:
    hum = 'high'
    pass


if temp == 'low' and hum == 'low':
    volume = 'medium'
elif temp == 'low' and hum == 'ideal':
    volume = 'low'
elif temp == 'low' and hum == 'high':
    volume = 'low'
elif temp == 'ideal' and hum == 'low':
    volume = 'medium'
elif temp == 'ideal' and hum == 'ideal':
    volume = 'medium'
elif temp == 'ideal' and hum == 'high':
    volume = 'low'
elif temp == 'high' and hum == 'low':
    volume = 'high'
elif temp == 'high' and hum == 'ideal':
    volume = 'high'
elif temp == 'high' and hum == 'high':
    volume = 'medium'


p = min(temp_pertinence, humidity_pertinence)

if volume == 'low':
    print(low_output.de_fuzzy([.0, 125], p))
elif volume == 'medium':
    print(medium_output.de_fuzzy([125, 375], p))
elif volume == 'high':
    print(high_output.de_fuzzy([375, 500], p))
