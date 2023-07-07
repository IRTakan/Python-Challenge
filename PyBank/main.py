import os
import csv
import pandas as pd

# Load CSV into a DataFrame
df = pd.read_csv("../Resources/PyBankResource/budget_data.csv")

# Import CSV file to terminal
#print(df.to_string())

print("\n")
print("Financial Analysis")
print("\n-------------------------")

# Total Months
total_months = df['Date'].count()
print("\nTotal Months:", total_months)

# Total Profit/Loss
total_profit_loss = df['Profit/Losses'].sum()
print("\nTotal: $" + str(total_profit_loss))

# Average Change in Profit/Loss
df['Change'] = df['Profit/Losses'].diff()
avg_change = df['Change'].mean()
print("\nAverage Change: $" + str(round(avg_change, 2)))

# Greatest Increase in Profits
greatest_increase = df['Change'].max()
greatest_increase_date = df.loc[df['Change'] == greatest_increase, 'Date'].iloc[0]
print(f"\nGreatest Increase in Profits: {greatest_increase_date} (${str(round(greatest_increase))})")

# Greatest Decrease in Profits
greatest_decrease = df['Change'].min()
greatest_decrease_date = df.loc[df['Change'] == greatest_decrease, 'Date'].iloc[0]
print(f"\nGreatest Decrease in Profits: {greatest_decrease_date} (${str(round(greatest_decrease))})")

# Biggest Profit and Loss
biggest_profit = df['Profit/Losses'].max()
biggest_profit_date = df.loc[df['Profit/Losses'] == biggest_profit, 'Date'].iloc[0]
print(f"\nBiggest Profit: {biggest_profit_date} (${str(biggest_profit)})")

biggest_loss = df['Profit/Losses'].min()
biggest_loss_date = df.loc[df['Profit/Losses'] == biggest_loss, 'Date'].iloc[0]
print(f"\nBiggest Loss: {biggest_loss_date} (${str(biggest_loss)})")

# Volatility Analysis
volatility = df['Profit/Losses'].std()
print("\nProfit/Loss Volatility: $" + str(round(volatility, 2)))

# Percentage Change
df['Percentage Change'] = df['Profit/Losses'].pct_change()*100
average_percentage_change = df['Percentage Change'].mean()
print("\nAverage Percentage Change: " + str(round(average_percentage_change, 2)) + "%")
print("\n")


# Export results as a text file
file = open('PyBank.txt', 'w')

s1 = str("Financial Analysis") + "\n"
s2 = str("\n-------------------------") + "\n"
s3 = str("\nTotal Months: ") + str(total_months) + "\n"
s4 = str("\nTotal: $ ") + str(total_profit_loss) + "\n"
s5 = str("\nAverage Change: $") + str(round(avg_change, 2)) + "\n"
s6 = str(f"\nGreatest Increase in Profits: {greatest_increase_date} (${str(greatest_increase)})") + "\n"
s7 = str(f"\nGreatest Decrease in Profits: {greatest_decrease_date} (${str(greatest_decrease)})") + "\n"
s8 = str(f"\nBiggest Profit: {biggest_profit_date} (${str(biggest_profit)})") + "\n"
s9 = str(f"\nBiggest Loss: {biggest_loss_date} (${str(biggest_loss)})") + "\n"
s10 = str("\nProfit/Loss Volatility: $" + str(round(volatility, 2))) + "\n"
s11 = str("\nAverage Percentage Change: " + str(round(average_percentage_change, 2)) + "%") + "\n"

l1 = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11]
file.writelines(l1)
file.close()

    