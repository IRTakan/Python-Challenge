import os
import csv

# Set path for CSV File
csvpath = 'Python-Challenge/Resources/PyBankResource/budget_data.csv'

# Lists to hold output of each variable
dates = []
diff_profits_losses = []

# Counters for variables
n_total = 0
t_months = 0
profits_losses  = 0
changes_month = 0

# First and second row varibales
f_row = 0
s_row = 0

# Read CSV file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skipping first header row
    next(csvreader)

    # Loop through CSV file
    for row in csvreader:
        t_months +=1

        # The net total of Profit/Losses
        f_row = int(row[1])
        n_total += int(row[1])

        # Loop through average changes in Profits/Losses
        if (t_months == 1):
            s_row = f_row
        else:
            changes_month = f_row - s_row
            dates.append(row[0])
            diff_profits_losses.append(changes_month)
            s_row = f_row

    # Calculate the average change
    a_change = round(sum(diff_profits_losses)/len(diff_profits_losses), 2)
        
    # Finding the date with greatest increase
    g_increase = max(diff_profits_losses)
    i_date = dates[diff_profits_losses.index(g_increase)]

    # Finding the date with greatest decrease
    g_decrease = min(diff_profits_losses)
    d_date = dates[diff_profits_losses.index(g_decrease)]


    print(f'\nFinancial Analysis')
    print(f'\n---------------------')
    print(f'\nTotal Months:', t_months)
    print(f'\nTotal:  ${str(round(n_total))}')
    print(f'\nAverage Change: ${str(a_change)}')
    print(f'\nGreatest Increase in Profits: {i_date} (${str(round(g_increase))})')
    print(f'\nGreatest Decrease in Profits: {d_date} (${str(round(g_decrease))})')
    print('\n')


# Export results as a text file
file = open('PyBank.txt', 'w')

s1 = str(f'\nFinancial Analysis') + "\n"
s2 = str(f'\n-------------------------') + "\n"
s3 = str(f'\nTotal Months:' + str(t_months)) + "\n"
s4 = str(f'\nTotal:  ${str(round(n_total))}') + "\n"
s5 = str(f'\nAverage Change: ${str(a_change)}') + "\n"
s6 = str(f'\nGreatest Increase in Profits: {i_date} (${str(round(g_increase))})') + "\n"
s7 = str(f'\nGreatest Decrease in Profits: {d_date} (${str(round(g_decrease))})') + "\n"

l1 = [s1, s2, s3, s4, s5, s6, s7]
file.writelines(l1)
file.close()

    
