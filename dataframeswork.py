import pandas as pd

df = pd.read_csv("usa_mercedes_benz_prices.csv") #reading from file

#converting mileage, price and review count strings to int
df['Mileage'] = df['Mileage'].str.replace(',', '')
df['Mileage'] = df['Mileage'].str.replace(' mi.', '')

df = df[df['Price'] != 'Not Priced']
df['Price'] = df['Price'].str.replace(',','')
df['Price'] = df['Price'].str.replace('$','')
df['Price'] = pd.to_numeric(df['Price'])

df['Review Count'] = df['Review Count'].str.replace(',','')
df['Review Count'] = df['Review Count'].str.replace(' ','')
df['Review Count'] = pd.to_numeric(df['Review Count'])

#mean, mode, median == average, most repeated, middle
meanPrice = df['Price'].mean()
print("Mean of the prices is: ", meanPrice)

medianPrice = df['Price'].median()
print("Median of the prices is: ", medianPrice)

#maximum, minimum
maxPrice = df['Price'].max()
print("Maximum price is: ", maxPrice)

minPrice = df['Price'].min()
print("Minimum price is: ", minPrice)

#total count, distinct count
totalCount = df['Review Count'].count()
print("Total Count is: ", totalCount)

distinctCount = df['Review Count'].nunique()
print("Distinct Count is: ", distinctCount)

#75th percentile
percentile = df['Price'].quantile(0.75)
print("75th percentile of price is: ", percentile)