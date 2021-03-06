# Import pandas as pd
from operator import index
from tkinter import N
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
difference = [0]

# Start for loop
for x in range(1, len(df)):
    difference.append(df["Profit/Losses"][x] - df["Profit/Losses"][x-1])

df["differences"]=difference

print(df["differences"][1:].mean())

# Get the greatest increase/greatest decrease
great_inc = (df["differences"].max())
great_dec = (df["differences"].min())

# Calculate the greatest month/decrease month
greatmonth = df.loc[df["differences"] == great_inc]["Date"].to_list()[0]
greatdec = df.loc[df["differences"] == great_dec]["Date"].to_list()[0]


print("Financial Analysis")
print("------------------")
print("Total Months", (len(df)))
print("Total $", ((df["Profit/Losses"].sum())))
print("Average Change $" , (df["differences"][1:].mean()))
print("Greatest Increase in Profits: $", (greatmonth), (great_inc))
print("Greatest Decrease in Profits: $", (greatdec), ((great_dec)))

file = open('pybank.txt','a')
file.write('\nFinancial Analysis')
file.write('\n-------------------')
file.write("\nTotal Months", (len(df)))
file.write("\nTotal", ((df["Profit/Losses"].sum())))
file.write("\nAverage Change $" , (df["differences"][1:].mean()))
file.write("\nGreatest Increase in Profits: $", (greatmonth), (great_inc))
file.write("\nGreatest Decrease in Profits: $", (greatdec), ((great_dec)))
file.close()