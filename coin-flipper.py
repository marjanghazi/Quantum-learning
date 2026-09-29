import math
import random

# Quantum coin in equal superposition
amplitude_0 = 1 / math.sqrt(2)
amplitude_1 = 1 / math.sqrt(2)

# Convert amplitudes to probabilities
probability_0 = amplitude_0 ** 2
probability_1 = amplitude_1 ** 2

print("Amplitude of |0>:", amplitude_0)
print("Amplitude of |1>:", amplitude_1)

print("Probability of measuring 0:", probability_0)
print("Probability of measuring 1:", probability_1)

# Measurement
result = random.choices(
    [0, 1],
    weights=[probability_0, probability_1]
)[0]

print("Measurement result:", result)