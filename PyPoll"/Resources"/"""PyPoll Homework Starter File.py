"""PyPoll Homework Starter File."""

# Import modules
import csv

# Files to load 
file_path = '''/Users/esteban/Desktop/Data Analyst BC/Module 3_Python/python-challenge/PyPoll"/Resources"/election_data.csv'''

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidate_votes = {}

# Open and read the CSV file
with open(file_path, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)  # Skip the header row
 # Loop through each row of the dataset and process it
    for row in csvreader:
        total_votes += 1
        candidate = row[2]  # Candidate is in the 3rd column

        # Count votes for each candidate
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1

     # Loop through the candidates to determine vote percentages and identify the winner

winner = ""
max_votes = 0
results = []

for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")
    
    if votes > max_votes:
        max_votes = votes
        winner = candidate


# Print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for result in results:
    print(result)
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Save results to a text file
output_path = 'election_results.txt'
with open(output_path, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for result in results:
        file.write(result + "\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")