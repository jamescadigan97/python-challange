#Import data
import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
election_csv = os.path.join(".", "Resources", "election_data.csv")

#Define lists and variables
vote = []
ballot = []
results = []
results_dict = {}
vote_count = 1

#Read csv file and skip header
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)


#Create a list of votes. Sort through list alphabetically to make it easier to count.
    for row in csvreader:
        vote.append(row[2])
    vote.sort(key=str.lower)

#Define variable 
    total_votes = len(vote)

#Since all the votes of the same people are next to each other, this finds unique names
    for x in range (0, total_votes-1):
        if vote[x-1] != vote[x]:
            ballot.append(vote[x])

#Define Variable
    num_c = len(ballot)

#Since the vote list is aphabetical, all the votes for the candidates will be next to each other. 
#The count starts at 1 because the last vote isn't picked up by the counter
    for x in range (0, total_votes - 1):
        if vote[x] == vote[x+1]:
            vote_count = vote_count + 1
        elif vote[x] != vote[x+1]:
            results.append(vote_count)
            vote_count = 1.0
    results.append(vote_count)
    winner = max(results)

    #Created a dictionary linking the candidates to there votes
    for x in range (0,num_c):
        results_dict.update( {ballot[x]: results[x]} )

    #Ordered list from most votes to least votes
    dict_keys = results_dict.items()
    sorted_results = sorted(dict_keys,key=lambda x: x[1], reverse=True)

    #Print results
    print("                          ")
    print("Election Results")
    print("------------------------")
    print("Total Votes: " + str(total_votes))
    print("------------------------")
    for x in range (0,num_c):
        print( sorted_results[x][0]+": " + "{:.2%}".format(sorted_results[x][1]/total_votes) + " ("+ str(sorted_results[x][1])+ ")" )
    print("------------------------")
    print("Winner: " +  sorted_results[0][0])
    print("                         ")
