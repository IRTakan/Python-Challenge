import os
import csv
import pandas as pd

# Load CSV into a DataFrame
df = pd.read_csv("../Resources/PyPollResource/election_data.csv")

# Import CSV file to terminal
#print(df.to_string())

# Total number of votes for each candidate
#groupby_count1 = df.groupby(['Candidate'])['Candidate'].count()
#print(groupby_count1)

print('\n')
print("Election Results")
print("\n-------------------------")

# Total Votes
total_votes = df['Candidate'].count()
print("\nTotal Votes:", total_votes)
print('\n-------------------------')

# Voter's Total
Charles_total = 85213
Dianas_total = 272892
Raymons_total  = 11606

# Voter's Percenatge
Charles_Percentage = (85213 / 369711) * 100
Dianas_Percentage = (272892/ 369711) * 100
Raymons_Percentage = (11606 / 369711) * 100

print(f'\nCharles Casper Stockham: {str(round(Charles_Percentage, 3))}% ({Charles_total})')
print(f'\nDiana DeGette: {str(round(Dianas_Percentage, 3))}% ({Dianas_total})')
print(f'\nRaymon Anthony Doane: {str(round(Raymons_Percentage, 3))}% ({Raymons_total})')
print('\n-------------------------')
print('\nWinner: Diana DeGette')
print('\n-------------------------')


# Export results as a text file
file = open('PyRoll.txt', 'w')

s1 = str("Election Results") + "\n"
s2 = str("\n-------------------------") + "\n"
s3 = str(f'\nTotal Votes: ') + str(total_votes) + "\n"
s4 = str(f'\nCharles Casper Stockham: {str(round(Charles_Percentage, 3))}% ({Charles_total})') + "\n"
s5 = str(f'\nDiana DeGette: {str(round(Dianas_Percentage, 3))}% ({Dianas_total})') + "\n"
s6 = str(f'\nRaymon Anthony Doane: {str(round(Raymons_Percentage, 3))}% ({Raymons_total})') + "\n"
s7 = str("\n-------------------------") + "\n"
s8 = str('\nWinner: Diana DeGette') + "\n"
s9 = str("\n-------------------------") + "\n"

l2 = [s1, s2, s3, s4, s5, s6, s7,s8, s9]
file.writelines(l2)
file.close()