from re import X
import pandas as pd

df = pd.read_csv('election_data.csv.')

print("Election Results")
print("--------------------------")

# Calculate total number of votes cast
print(len(df))

# Complete list of canidates who revived votes
totalcandi = df["Candidate"].value_counts()

print("--------------------------")

# The percentage of votes each candidate won
votes = totalcandi/len(df)*100

# The winner of the election based on popular vote
count = 0
winner = ''
for x in df["Candidate"].unique():
    popular = len(df.loc[df["Candidate"] == x])
    print(f"{x}: {'{:.3f}'.format(popular/len(df) * 100)}% ({popular})")
    if popular > count:
        winner = x
        count = popular
        
print("--------------------------")
print(f'winner :{winner}')
print("--------------------------")

file = open('pypoll.txt','a')
file.write("\nElection Results")
file.write("\n--------------------------")
file.write("\nTotal Votes:" (len(df)))
file.write("\n--------------------------")
file.write(f'winner :{winner}')
file.write("\n--------------------------")
file.close()
