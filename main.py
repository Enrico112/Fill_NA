import pandas as pd

df = pd.read_csv('melbourne_housing.csv')
df.shape
df.nunique()

# retain cols to use
cols_to_use = ['Suburb', 'Rooms', 'Type', 'Method', 'SellerG', 'Regionname', 'Propertycount',
               'Distance', 'CouncilArea', 'Bedroom2','Bathroom', 'Car', 'Landsize', 'BuildingArea', 'Price']
df = df[cols_to_use]

# count nas in every col
df.isna().sum()

# cols to fill with zero
cols_fill_zero = ['Propertycount', 'Distance', 'Bedroom2', 'Bathroom', 'Car']
df[cols_fill_zero] = df[cols_fill_zero].fillna(0)

# cols to fill with mean
df['Landsize'] = df['Landsize'].fillna(df.Landsize.mean())
df['BuildingArea'] = df['BuildingArea'].fillna(df.Landsize.mean())

# drop remaining nas in price
df.dropna(inplace=True)