from math import exp


class FuzzySet:
    TRIANGULAR = 0
    TRAPEZOIDAL = 1
    SINUSOIDAL = 2

    def __init__(self, set_type, values):
        self.type = set_type

        self.values = values

    def calculate_pertinence(self, value):
        if self.type == 0:
            return self._calculate_triangular_pertinence(value)
        elif self.type == 1:
            return self._calculate_trapezoidal_pertinence(value)
        else:
            return self._calculate_sinusoidal_pertinence(value)

    def _calculate_triangular_pertinence(self, value):
        if value <= self.values[0]:
            return .0
        elif self.values[0] < value <= self.values[1]:
            return (value - self.values[0]) / (self.values[1] - self.values[0])
        elif self.values[1] <= value <= self.values[2]:
            return (value - self.values[2]) / (self.values[1] - self.values[2])
        else:
            return .0

    def _calculate_trapezoidal_pertinence(self, value):
        if self.values[0] <= value < self.values[1]:
            return (value - self.values[0]) / (self.values[1] - self.values[0])
        elif self.values[1] <= value <= self.values[2]:
            return 1.0
        elif self.values[2] < value <= self.values[3]:
            return (self.values[3] - value) / (self.values[3] - self.values[2])
        else:
            return .0

    def _calculate_sinusoidal_pertinence(self, value):
        if (self.values[1] - self.values[2]) <= value <= (self.values[1] + self.values[2]):
            return exp((-pow((value - self.values[1]), 2.0)) / self.values[0])
        else:
            return .0

    def de_fuzzy(self, values):
        sum_a = 0
        sum_b = 0

        for value in values:
            pertinence = self.calculate_pertinence(value)

            sum_a += (value * pertinence)
            sum_b += pertinence

        return sum_a / sum_b



