#importing modules and libraries 
import os
import csv

#creating object from csv file 
budgetData = os.path.join(".","Resources","budget_data.csv")

#open and reading csv file 
with open(budgetData, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
    #reading data in rows
    data = list(csvreader)
    row_count = len(data)
    total = 0
    
    #calculate change in row
    for i in range(0, row_count):
        total = total + int(data[i][1])
    num1 = 0
    num2 = int(data[0][1])
    diff = 0
    difflist = list()
    #calculate change in column 
    for j in range(1, row_count):
        num1 = int(data[j][1])
        diff = num1 - num2
        difflist.append(diff)
        num2 = int(data[j][1])
        
        #max increase, lowest increase, average change
    avgChange = round(sum(difflist)/len(difflist),2)
    maxDiff = max(difflist)
    maxDiffPos = difflist.index(maxDiff)+1
    minDiff = min(difflist)
    minDiffPos = difflist.index(minDiff)+1
    
    #Display Analysis to Terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {row_count}")
    print(f"Total: ${total:,}")
    print(f"Average Change: ${avgChange:,}")
    print(f"Greatest Increase in Profits: {data[maxDiffPos][0]} (${maxDiff:,})")
    print(f"Greatest Decrease in Profits: {data[minDiffPos][0]} (${minDiff:,})")
    
    #Create "PyBank.txt" file
    print("Financial Analysis", file=open("PyBank.txt", "a"))
    print("----------------------------", file=open("PyBank.txt", "a"))
    print(f"Total Months: {row_count}", file=open("PyBank.txt", "a"))
    print(f"Total: ${total:,}", file=open("PyBank.txt", "a"))
    print(f"Average Change: ${avgChange:,}", file=open("PyBank.txt", "a"))
    print(f"Greatest Increase in Profits: {data[maxDiffPos][0]} (${maxDiff:,})", file=open("PyBank.txt", "a"))
    print(f"Greatest Decrease in Profits: {data[minDiffPos][0]} (${minDiff:,})", file=open("PyBank.txt", "a"))