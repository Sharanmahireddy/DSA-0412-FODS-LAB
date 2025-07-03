import pandas as pd

property_data = pd.DataFrame({
    'property_id': [101, 102, 103, 104],
    'location': ['CityA', 'CityB', 'CityA', 'CityB'],
    'bedrooms': [3, 5, 6, 4],
    'area_sqft': [1500, 2000, 2500, 1800],
    'listing_price': [300000, 450000, 500000, 350000]
})

# 1. Avg listing price by location
avg_price_by_location = property_data.groupby('location')['listing_price'].mean()

# 2. Properties with >4 bedrooms
more_than_4_bedrooms = property_data[property_data['bedrooms'] > 4].shape[0]

# 3. Property with largest area
largest_area_property = property_data.loc[property_data['area_sqft'].idxmax()]

print("Average price by location:\n", avg_price_by_location)
print("Number of properties with >4 bedrooms:", more_than_4_bedrooms)
print("Property with largest area:\n", largest_area_property)
