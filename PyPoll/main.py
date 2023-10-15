# Import
import os
import csv

# CSV File Path
csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")

# Declare Variables 
total_votes = 0
Charles_Casper_Stockham_votes = 0
Diana_DeGette_votes = 0
Raymon_Anthony_Doane_votes = 0

# Open csv in using UTF-8
with open(csvpath, encoding="utf-8") as elections:

    # Store data under the csvreader 
    csvreader = csv.reader(elections,delimiter=",") 

    # Skip the header so we move through the actual values
    header = next(csvreader)     

    # each row in the csv
    for row in csvreader: 

        # Count the unique Ballot ID's and store in variable  called total_votes
        total_votes +=1

        # use this values in our percent vote calculation in the print statements
        if row[2] == "Charles Casper Stockham": 
            Charles_Casper_Stockham_votes +=1
        elif row[2] == "Diana DeGette":
            Diana_DeGette_votes +=1
        elif row[2] == "Raymon Anthony Doane": 
            Raymon_Anthony_Doane_votes +=1

 # To find the winner need to make a dictionary out of the two lists we previously created 
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [Charles_Casper_Stockham_votes, Diana_DeGette_votes, Raymon_Anthony_Doane_votes]

# Now put together the list of candidates and the total votes
# Return the winner using a max function of the dictionary 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Print a summary of the analysis
Charles_Casper_Stockham_percent = (Charles_Casper_Stockham_votes/total_votes) * 100
Diana_DeGette_percent = (Diana_DeGette_votes/total_votes) * 100
Raymon_Anthony_Doane_percent = (Raymon_Anthony_Doane_votes/total_votes) * 100

# Print the summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {Charles_Casper_Stockham_percent:.3f}% ({Charles_Casper_Stockham_votes})")
print(f"Diana DeGette: {Diana_DeGette_percent:.3f}% ({Diana_DeGette_votes})")
print(f"Raymon Anthony Doane: {Raymon_Anthony_Doane_percent:.3f}% ({Raymon_Anthony_Doane_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

# Output files
# Assign output file location
output_file = os.path.join("PyPoll", "analysis" , "Election_Results.txt")

with open(output_file,"w+") as file:

# Write methods to print to Elections_Results 
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {Charles_Casper_Stockham_percent:.3f}% ({Charles_Casper_Stockham_votes})")
    file.write("\n")
    file.write(f"Diana DeGette: {Diana_DeGette_percent:.3f}% ({Diana_DeGette_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {Raymon_Anthony_Doane_percent:.3f}% ({Raymon_Anthony_Doane_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")



