import os

import csv

num_ballots = 0
candidates = []
ballot_count = []

csvpath = os.path.join('PyPoll', 'election_data.csv')
with open(csvpath, encoding = "utf-8-sig") as csvfile:  

    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])
            ballot_count.append(1)
        else:
            pos = candidates.index(row[2])
            ballot_count[pos] += 1
        num_ballots += 1

max_ballots = -1
candidates.pop(0)
ballot_count.pop(0)
# print(candidates,ballot_count)
report_path = os.path.join('PyPoll', 'election_data_report.txt')
with open(report_path, "w") as report_file: 
    print("Election Results")
    report_file.write(f"Election Results\n")
    print("Total Votes:", num_ballots - 1)
    report_file.write(f"Total Votes: {num_ballots - 1}\n")
    for i in range (len(candidates)):
        percent = 100.0 * ballot_count[i]/(num_ballots - 1)
        percent = round(percent,3)
        print(f"{candidates[i]}: {percent}% ({ballot_count[i]})")
        report_file.write(f"{candidates[i]}: {percent}% ({ballot_count[i]})\n")
        if ballot_count[i] > max_ballots:
            max_ballots = ballot_count[i]
            max_index = i
        #report_file.write(f"total profit is: ${total_profit:,} and greatest increase in profit is: ${max_profit:,}\n")

    print(f"Winner: {candidates[max_index]}")
    report_file.write(f"Winner: {candidates[max_index]}")
        
        
#Winner: Diana DeGette