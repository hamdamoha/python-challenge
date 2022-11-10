import os
import csv


csvpath = os.path.join("Resources", "election_data.csv")
csvpath = "//Users//hamda//Documents//python-challenge//PyPoll//Resources//election_data.csv"



candidates = []
votes = []
county = []
Charles = []
Diana = []
Rayman = []


#Retrieve Data from election_data.csv to create three columns: `Voter ID`, `County`, and `Candidate`
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Read each row of data after the header and loop through rows
    for row in csvreader:
        votes.append(row[0])
        county.append(row[1])
        candidates.append(row[2])
        
    # The total number of votes cast
        voter_total = len(row [1])

    # A complete list of candidates who received votes and the total number of votes each candidate won.
        for can in candidates:
            if can == "Charles":
                Charles.append(candidates)
                votes_Charles= len(Charles)
            elif can == "Diana":
                Diana.append(candidates)
                votes_Diana = len(Diana)
            else  == "Rayman":
                Rayman.append(candidates)
                votes_Rayman = len(Rayman)
        

    # The percentage of votes each candidate won.
    per_Charles = round(((votes_Charles / voter_total) * 100), 2)
    per_Diana = round(((votes_Diana / voter_total) * 100), 2)
    per_Rayman = round(((votes_Rayman / voter_total) * 100), 2)
    

    # The winner of the election based on popular vote.
    def winner(candidates):
        return max(set(candidates), key = candidates.count)

# Print the analysis to the terminal.


print("Election Results")
print("----------------------------")
print(f"Total votes:  {votes}")
print("----------------------------")
print(f"Charles: %{per_Charles} ({votes_Charles})")
print(f"Diana: %{per_Diana} ({votes_Diana})")
print(f"Rayman: %{per_Rayman} ({votes_Rayman})")
print("----------------------------")
print(f"Winner: ({winner})")
print("----------------------------")

#  Export a text file with the results to Analysis folder.
with open(__path__, "w") as results:
    results.write("Election Results\n")
    results.write("----------------------------\n")
    results.write(f"Total votes:  {votes}\n")
    results.write("----------------------------\n")
    results.write(f"Charles: %{per_Charles} ({votes_Charles})\n")
    results.write(f"Diana: %{per_Diana} ({votes_Diana})\n")
    results.write(f"Rayman: %{per_Rayman} ({votes_Rayman})\n")
    results.write("----------------------------\n")
    results.write(f"Winner: ({winner})\n")
    results.write("----------------------------\n")