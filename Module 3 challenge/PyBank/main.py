
#Import modules
import os
import csv

# Set and check path for CSV file from the module 3 folder
budgetData = os.path.join(".","Resources","budget_data.csv")
# currentDirectory = os.getcwd()
# print(currentDirectory)
# print(budgetData)

# Open the CSV file
with open(budgetData, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

  # The total number of months included in the dataset (row count after the header)
    next(csvreader)
    data = list(csvreader)
    row_count = len(data)

  # The net total amount of "Profit/Losses" over the entire period
    total = 0
    for i in range(0, row_count): 
        total = total + int(data[i][1]) 

  # The average of the changes in "Profit/Losses" over the entire period    
    number1 = 0
    number2 = int(data[0][1])
    diff = 0
    difflist = list()
    for j in range(1, row_count):
        number1 = int(data[j][1])
        diff = number1 - number2
        difflist.append(diff)
        number2 = int(data[j][1])
    avgChange = round(sum(difflist)/len(difflist),2)

  # The greatest increase in profits (date and amount) over the entire period *+1 accounts for difference in rows
    maxDiff = max(difflist)
    maxDiffPos = difflist.index(maxDiff)+1
    
  # The greatest decrease in losses (date and amount) over the entire period *+1 accounts for difference in rows
    minDiff = min(difflist)
    minDiffPos = difflist.index(minDiff)+1

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
  # Print the results to terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {row_count}")
    print(f"Total: ${total:,}")
    print(f"Average Change: ${avgChange:,}")
    print(f"Greatest Increase in Profits: {data[maxDiffPos][0]} (${maxDiff:,})")
    print(f"Greatest Decrease in Profits: {data[minDiffPos][0]} (${minDiff:,})")

  # Print the results to "PyBank.txt" file
    print("Financial Analysis", file=open("Analysis.txt", "a"))
    print("----------------------------", file=open("Analysis.txt", "a"))
    print(f"Total Months: {row_count}", file=open("Analysis.txt", "a"))
    print(f"Total: ${total:,}", file=open("Analysis.txt", "a"))
    print(f"Average Change: ${avgChange:,}", file=open("Analysis.txt", "a"))
    print(f"Greatest Increase in Profits: {data[maxDiffPos][0]} (${maxDiff:,})", file=open("Analysis.txt", "a"))
    print(f"Greatest Decrease in Profits: {data[minDiffPos][0]} (${minDiff:,})", file=open("Analysis.txt", "a"))