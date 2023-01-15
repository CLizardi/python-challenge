import csv
from collections import Counter

# Set file path
csvpath = 'resources\election_data.csv'

# Variables
total_votes = 0
candidate_votes = Counter()
candidates = set()

# Read  CSV file
with open(csvpath, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        total_votes += 1
        candidate = row['Candidate']
        candidates.add(candidate)
        candidate_votes[candidate] += 1

# Percentage of votes for each candidate
percentages = {candidate: round(votes / total_votes * 100, 3) for candidate, votes in candidate_votes.items()}

# The winner
winner = max(candidate_votes, key=candidate_votes.get)

# Print results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, percentage in percentages.items():
    print(f"{candidate}: {percentage}% ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export results to a text file
with open("newfile.txt", "w") as text_file:
    text_file.write("Election Results\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write("-------------------------\n")
    for candidate, percentage in percentages.items():
        text_file.write(f"{candidate}: {percentage}% ({candidate_votes[candidate]})\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Winner: {winner}\n")
    text_file.write("-------------------------\n")
