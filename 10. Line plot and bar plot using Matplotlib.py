import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [1000, 1500, 1200, 1700, 1800, 1600]

# Line plot
plt.figure(figsize=(8, 4))
plt.plot(months, sales, marker='o', linestyle='-', color='blue')
plt.title("Monthly Sales - Line Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.show()

# Bar plot
plt.figure(figsize=(8, 4))
plt.bar(months, sales, color='skyblue')
plt.title("Monthly Sales - Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()
