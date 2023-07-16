import os
import csv

# Set path for CSV File
csvpath = 'Python-Challenge/Resources/PyPollResource/election_data.csv'

# Lists to hold output of each variable
c_votes = {}
percentage_c_votes = {}
c_names = []

# Counter for variables
t_votes = 0
w_count = 0

# Read CSV file
with open(csvpath, newline ='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')

    # Skipping first header row
    csv_header = next(csvreader)

    for row in csvreader:
        # Add to vote-counter
        t_votes += 1 

        # Start loop to add candidate to the list
        if row[2] in c_names:
            c_votes[row[2]] +=1
        else:
            c_names.append(row[2])
            c_votes[row[2]] = 1

        # Work out the percentage of votes for each candidate
        for key, value in c_votes.items():
            percentage_c_votes[key] = round((value/t_votes) * 100, 3)

    #Pick the winner based off votes
    winner = max(percentage_c_votes, key=percentage_c_votes.get)


    # Print output into Terminal
    print('\nElection Results')
    print('\n---------------------')
    print('\nTotal Vote: ', str(t_votes))
    print('\n---------------------')

    for key, value in c_votes.items():
        print(f'\n{key} : {percentage_c_votes[key]}% ({c_votes[key]})')

    print(f'\n---------------------')
    print(f'\nWinner: {winner}')
    print(f'\n---------------------')


# Export results as a text file
file = open('PyPoll.txt', 'w')

l1 = []
s1 = str(f'\nElection Results') + "\n"
s2 = str(f'\n---------------------') + "\n"
s3 = str(f'\nTotal Vote: ' + str(t_votes)) + "\n"
s4 = str(f'\n---------------------') + "\n"
l1 = [s1, s2, s3, s4]

for key, value in c_votes.items():
    l1.append((f'\n{key} : {percentage_c_votes[key]}% ({c_votes[key]})'))
    l1.append((f'\n'))

s5 = str(f'\n---------------------') + "\n"
s6 = str(f'\nWinner: {winner}') + "\n"
s7 = str(f'\n---------------------') + "\n"
l1.append(s5)
l1.append(s6)
l1.append(s7)

file.writelines(l1)
file.close()
