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

#Open the elction results and read the file
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)

    #Print the header row.
    headers=next(file_reader)
    print(headers)


