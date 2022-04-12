# Import pandas as pd
from operator import index
import pandas as pd
import numpy as np

# Create dataframe
df = pd.read_csv('budget_data.csv')

# Print your data frame
print(df.head())

# List
print(df["Date"])

# Print the length of months
print(len(df))

# Print total of Profit/Losses with .sum
print(df["Profit/Losses"].sum())

difference= [0]

for x in range(1, len(df)):
    difference.append(df["Profit/Losses"][x] - df["Profit/Losses"][x-1])
df["differences"]=difference
print(df.head())




print("Financial Analysis")
print("------------------")
print("Total Months", (len(df)))
print("Total", ((df["Profit/Losses"].sum())))
print("Average Change", )
print("Greatest Increase in Profits:", )
print("Greatest Decrease in Profits:", )