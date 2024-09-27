import pandas as pd
import numpy as np
import math

df2 = pd.read_table("chipotle.txt", sep='\t', usecols=["item_price"])
# amountData = df.count()[0]

# print(df.columns)

priceList = df2['item_price'].values.tolist()

priceList = [priceList[i].strip('$') for i in range(len(priceList))]
priceList = [priceList[i].replace(" ","") for i in range(len(priceList))]

output = sorted(priceList, key = float)

sumOfNumbers = 0
for price in priceList:
    sumOfNumbers += float(price)


# Sum of all prices
print(f"Sum: {sumOfNumbers}")
# Average price
print(f"Average: {sumOfNumbers/len(priceList)}")
# Highest price
print(f"Highest: {output[-1]}")
# Lowest price
print(f"Lowest: {output[0]}")
# Number of items
print(f"Number of items: {len(priceList)}")
# Difference between highest and lowest price
print(f"Difference between highest and lowest price: {float(output[-1]) - float(output[0])}")