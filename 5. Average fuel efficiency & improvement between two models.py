import numpy as np

fuel_efficiency = np.array([25, 30, 28, 35, 40])  # mpg for different car models

average_efficiency = np.mean(fuel_efficiency)
improvement = ((fuel_efficiency[4] - fuel_efficiency[0]) / fuel_efficiency[0]) * 100

print("Average fuel efficiency:", average_efficiency)
print("Improvement from model 1 to model 5:", improvement, "%")
