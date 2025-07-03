import numpy as np

# Each row = a product, each column = price of a unit sold (3x3 example)
sales_data = np.array([
    [100, 150, 200],  # Product 1
    [80, 120, 160],   # Product 2
    [90, 110, 130]    # Product 3
])

# Average price of all units sold
average_price = np.mean(sales_data)

print("Average product price:", average_price)
