import numpy as np

# Columns: [bedrooms, square footage, sale price]
house_data = np.array([
    [3, 1500, 300000],
    [5, 2500, 500000],
    [6, 2800, 550000],
    [4, 2000, 400000]
])

filtered = house_data[house_data[:, 0] > 4]
average_sale_price = np.mean(filtered[:, 2])

print("Average sale price of houses with >4 bedrooms:", average_sale_price)
