#The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who got votes
#3. Total number of votes each candidate won
#4. Percentage of votes each candidate won
#5. The winner of the elction based on popular vote.

#Add our dependencies.
import csv
import os
#Assign a variable to load a file from a path
file_to_load = os.path.join("Resources","election_results.csv")

#Assign a vaariable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Add total vote counter
total_votes = 0

#Candidate Options
candidate_options = []

#Candidate Votes empty dictionary
candidate_votes = {}

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the elction results and read the file
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)

    #Print the header row.
    headers=next(file_reader)

    #Print each row in the CSV file
    for row in file_reader:

        #Add to the total vote count
        total_votes +=1

        #print the candidate name from each row.
        candidate_name= row[2]
        if candidate_name not in candidate_options:
            #add it to the list of candidates.
            candidate_options.append(candidate_name)
            #begin tracking that candidate's votes
            candidate_votes[candidate_name] = 0
        #add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#Determine the percentage of votes for each candidate by looping through the counts.

# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print out each candidate's name, vote count, and percentage of total votes to the terminal

    #determine winning vote count and candidate
    #determine if the votes is greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if true then set winning_count = votes and winning_percent = vote percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #and, set the winning_candidate equal to the candidate's name
        winning_candidate = candidate_name

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"--------------------------\n"
    f"winner: {winning_candidate}\n"
    f"winning vote count: {winning_count:,}\n"
    f"winning percentage: {winning_percentage:.1f}%\n"
    f"--------------------------")
print(winning_candidate_summary)




    


    



