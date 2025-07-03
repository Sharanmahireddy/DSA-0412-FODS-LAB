item_prices = [50, 100, 200]
quantities = [2, 1, 3]
discount_rate = 10  # in percent
tax_rate = 8        # in percent

subtotal = sum(p * q for p, q in zip(item_prices, quantities))
discounted = subtotal * (1 - discount_rate / 100)
total = discounted * (1 + tax_rate / 100)

print("Final total after discount and tax:", total)
