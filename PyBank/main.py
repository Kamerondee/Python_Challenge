# Import pandas as pd
from operator import index
import pandas as pd
import numpy as np

# Create dataframe
df = pd.read_csv('budget_data.csv')

# List
print(df["Date"])

# Print the length of months
print(len(df))

# Print total of Profit/Losses with .sum
print(df["Profit/Losses"].sum())

# Set counter to 0
difference= [0]

# Start for loop
for x in range(1, len(df)):
    difference.append(df["Profit/Losses"][x] - df["Profit/Losses"][x-1])

df["differences"]=difference

print(df["differences"][1:].mean())
print(df.head())

great_inc = (df["differences"].max())
great_dec = (df["differences"].min())



print("------------------")
print("Financial Analysis")
print("------------------")
print("Total Months", (len(df)))
print("Total", ((df["Profit/Losses"].sum())))
print("Average Change", (df["differences"][1:].mean()))
print("Greatest Increase in Profits: $", [great_inc])
print("Greatest Decrease in Profits: $", (great_dec))