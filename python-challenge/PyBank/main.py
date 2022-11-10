#  Import the os module and the csv module
import csv
import os

# Set data path
csvpath = os.path.join("Resources","budget_data.csv")
csvpath = "//Users//hamda//Documents//python-challenge//PyBank//Reources//budget_data.csv"

# Variables to store data
number_line = 0
profitloss = []
profitloss_dates = []
profitloss_sum = 0
max_pl = 0
min_pl = 0
sum = 0

# Open path
with open(csvpath, 'r') as csvfile:
    
    print(type(csvfile))
    
    csv_reader = csv.reader(csvfile, delimiter = ',')
    
    print(type(csv_reader))
    
    header = next(csv_reader)
    print(f"{header}")

# Reach each row of data after the header and assign variables    
    for row in csv_reader:
        print(row)
        number_line += 1
        profitloss.append(int(row[1]))
        profitloss_sum += int(row[1])
        profitloss_dates.append(row[0])
        
    
profitloss_change = []

for i in range(1, len(profitloss)):
    x = profitloss[i] - profitloss[i - 1]
    profitloss_change.append(int(x))
    
    print(profitloss_change)

for i in range(0, len(profitloss_change)):
    sum += profitloss_change[i]
    average_change_profitloss = round((sum / (len(profitloss_change))), 2)

    print(average_change_profitloss)

for profloss in profitloss:
    
    if min_pl == 0:
        max_pl == profloss
        min_pl == profloss
    if profloss > max_pl:
        max_pl = profloss
    elif profloss < min_pl:
        min_pl = profloss
        
    print(max_pl, min_pl)

max_pl_index = profitloss.index(max_pl)
min_pl_index = profitloss.index(min_pl)

max_pl_date = profitloss_dates[max_pl_index]
min_pl_date = profitloss_dates[min_pl_index]

# Print the anaylysis to the terminal
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {number_line} ")
print(f"Total: ${profitloss_sum}")
print(f"Average Change: ${average_change_profitloss}")
print(f"Greatest Increase in Profits: ${max_pl} on {max_pl_date}")
print(f"Greatest Decrease in Profits: ${min_pl} on {min_pl_date}")

#Export a text file with the results to Analysis folder
pathout = ('Financial_Analysis.txt')
with open(pathout, 'w') as file:
    file.write(f"Financial Analysis\n")
    file.write(f"----------------------------\n")
    file.write(f"Total Months: {number_line} \n")
    file.write(f"Total: ${profitloss_sum}\n")
    file.write(f"Average Change: ${average_change_profitloss}\n")
    file.write(f"Greatest Increase in Profits: {max_pl_date} (${max_pl}) \n")
    file.write(f"Greatest Decrease in Profits: {min_pl_date} (${min_pl}) \n")
