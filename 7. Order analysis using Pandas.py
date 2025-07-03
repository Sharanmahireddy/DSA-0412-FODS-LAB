import pandas as pd

order_data = pd.DataFrame({
    'customer_id': [1, 2, 1, 3, 2, 1],
    'order_date': pd.to_datetime(['2024-06-01', '2024-06-03', '2024-06-05',
                                   '2024-06-10', '2024-06-15', '2024-06-20']),
    'product_name': ['A', 'B', 'A', 'C', 'B', 'C'],
    'order_quantity': [2, 1, 3, 4, 2, 1]
})

# 1. Total number of orders per customer
orders_per_customer = order_data['customer_id'].value_counts()

# 2. Average quantity per product
avg_order_quantity = order_data.groupby('product_name')['order_quantity'].mean()

# 3. Earliest and latest order dates
earliest_date = order_data['order_date'].min()
latest_date = order_data['order_date'].max()

print("Total orders per customer:\n", orders_per_customer)
print("Average order quantity per product:\n", avg_order_quantity)
print("Earliest order date:", earliest_date)
print("Latest order date:", latest_date)
