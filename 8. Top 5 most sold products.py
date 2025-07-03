import pandas as pd

df = pd.DataFrame({
    'product_name': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'D', 'E', 'B'],
    'quantity_sold': [10, 5, 8, 7, 9, 6, 3, 12, 4, 2]
})

top_5_products = df.groupby('product_name')['quantity_sold'].sum().sort_values(ascending=False).head(5)
print("Top 5 products sold:\n", top_5_products)
