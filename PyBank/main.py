# Import pandas as pd
import pandas as pd
import numpy as np

# Create dataframe
df = pd.read_csv('budget_data.csv')

print(df.head())

# List
print(df["Date"])

print(len(df))

print(df["Profit/Losses"].sum())





print("Financial Analysis")
print("---------------------")
print("Total Months", (len(df)))
print("Total", ((df["Profit/Losses"].sum())))
print("Average Change")