import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_table("chipotle.txt", sep='\t')

df['item_price'] = df['item_price'].str.replace('$', '').str.replace(' ', '').astype(float)

priceList = df['item_price'].values.tolist()
priceList.sort()

print(f"Sum: {df['item_price'].sum()}")
print(f"Average: {df['item_price'].mean()}")
print(f"Highest: {df['item_price'].max()}")
print(f"Lowest: {df['item_price'].min()}")
print(f"Number of items: {len(df)}")
print(f"Difference between highest and lowest price: {df['item_price'].max() - df['item_price'].min()}")
print(f"Median: {df['item_price'].median()}")
print(f"Standard deviation: {df['item_price'].std()}")
print("--------------------")
print(df.info())
print("--------------------")

plt.plot(priceList, 'ro')
plt.ylabel('Price')
plt.xlabel('Index')

a = df.index.to_list()
b = priceList
c = [.1*x for x in range(0,len(priceList)*10)]

coef = np.polyfit(a,b,2)
poly1d_fn = np.poly1d(coef)

plt.plot(a,b, 'go', c, poly1d_fn(c), '-')

plt.show()

print(df.nlargest(10, 'item_price'))