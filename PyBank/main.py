import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
budget_csv = os.path.join(".", "Resources", "budget_data.csv")

#Name Variables, Lists and Dictionaries
change_list = []
budget_list = []
months_list = []
months = {}
monthschange = {}
total_profits = 0.0
total_change = 0.0
total_months = 0

#Opened csv
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

#Ran through csv. Created lists for profits and months and a dictionary
    for row in csvreader:
        budget_list.append(row[1])
        months_list.append(row[0])
        months.update( {row[1]: [row[0]]})
    total_months = len(budget_list)

#Found total profit
    for row in budget_list:
        total_profits = int(budget_list[0]) + total_profits
    #total_months = len(budget_list)

#Found changes and made a list of them
    for x in range (1, int(total_months)):
        change_profits = int(budget_list[x]) - int(budget_list[x-1])
        change_list.append(change_profits)
        monthschange.update( {change_profits: months_list[x]} )

#Found total change and average change
    for row in change_list:
        total_change = total_change + int(change_list[0])
    av_change = total_change / total_months

#Found the greatest increase and decrease in profit. In analysis, accessed the months from dictionary
    maxchange = max(change_list)
    minchange = min(change_list)

#Print Aanalysis
    print("                    ")
    print("Financial Analysis")
    print("-------------------")
    print("Total Months: " + str(total_months))
    print("Total Profit: " + str(total_profits))
    print("Average Change: " + str(av_change))
    print("Greatest Increase in Profits: " + str(monthschange[maxchange]) + " (" + str(maxchange) + ") ")
    print("Greatest Decrease in Profits: " + str(monthschange[minchange]) + " (" + str(minchange) + ") ")
    print("                    ")