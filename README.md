# Python-Challenge

The Python challenge presents the task of creating a script that analyzes financial records of my company. If the execution is successful it should present
this output error free:

The total number of months.

The net total amount of "Profit/Losses" over the entire period.

The changes in "Profit/Losses" over the entire period, and then the average of those changes.

The greatest increase in profits (date and amount) over the entire period.

The greatest decrease in profits (date and amount) over the entire period.

Additional code has also been added to export the results to a text file.


*Technologies used: Microsoft Visual Studio Code.

*How to activate code: The files for each dataset sit in the 'PyBank' and PyPoll
folders under the name 'main.py'. You can open these files in your preferred Python
IDEs and run the script.

Notes: For both scripts I ran a code that imported the contents of the CSV files into
the terminal so that I could analayze it.

--budget_data.csv--
# Load the CSV into a DataFrame
df = pd.read_csv("C:/Users/robta/Desktop/GWDataAnalytics/DataAnalyticsBootcamp/
Module3Challenge/Python-Challenge/Resources/PyBankResource/budget_data.csv")

# Importing the csv file in terminal
#print(df.to_string())

--election_data.csv--

# Load the CSV into a DataFrame
df = pd.read_csv("C:/Users/robta/Desktop/GWDataAnalytics/DataAnalyticsBootcamp/
Module3Challenge/Python-Challenge/Resources/PyPollResource/election_data.csv")

# Importing the csv file in terminal
#print(df.to_string())

#Total votes for each candidate
#groupby_count1 = df.groupby(['Candidate'])['Candidate'].count()
#print(groupby_count1) --- (This showed me the total number of votes for each 
candidate.)

*Comment: Even though the challenge doesn't ask for it, I decided to add the results for:

Biggest Profit and Loss.

Volatility Analysis. 

Percentage Change.
