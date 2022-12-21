import os
from statistics import mean
import csv

total_months = 0
total_profit = 0
change = 0
previous_month = 0
changes = []
max_change = 0
max_change_month = ""
min_change = 0
min_change_month = ""

csvpath = os.path.join('PyBank', 'budget_data.csv')

with open(csvpath, encoding = "utf-8-sig") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvfile)
    print(f"header:{header}")

    for row in csvreader:
        print(row)

        profit = int(row[1])
        total_months = total_months + 1
        total_profit = total_profit + profit
        change = profit - previous_month
        if total_months != 1:
           changes.append(change)
        if change > max_change:
            max_change = change
            max_change_month = row[0]
        if change < min_change:
            min_change = change
            min_change_month = row[0]
        previous_month = profit

report_path = os.path.join('PyBank', 'budget_data_report.txt')
with open(report_path, "w") as report_file: 
    print(f"Total Months: {total_months:,}\n")
    report_file.write(f"Total Months: {total_months:,}\n")
    print(f"Total: ${total_profit:,}\n")
    report_file.write(f"Total: ${total_profit:,}\n")
    print(f"Average Change: ${int(mean(changes)):,}\n")
    report_file.write(f"Average Change: ${int(mean(changes)):,}\n")
    print(f"Greatest increase in Profits: ${max_change:,} ({max_change_month})\n")
    report_file.write(f"Greatest increase in Profits: ${max_change:,} ({max_change_month})\n")
    print(f"Greatest decrease in Profits: ${min_change:,} ({min_change_month})\n")
    report_file.write(f"Greatest decrease in Profits: ${min_change:,} ({min_change_month})\n")

