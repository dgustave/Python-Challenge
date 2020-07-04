import os
import csv

# Specify the file to write to
csvpath=os.path.join('..', '..', 'gt-atl-data-pt-06-2020-u-c', 'DataViz-Content', '03-Python', 'Homework', 'Instructions', 'PyPoll', 'Resources', 'election_data.csv')

with open(csvpath, 'r') as file:
    poll = csv.reader(file)
    next(poll)
    
    # intitial value to hold all votes

    #Create empty list to hold values
    delegates = [] #print all names
    percent = [] #print percent of votes
    vote_count = [] #total votes for each canidate
    ballots = [] # holds percent of votes for each canidates
    candidates = [] #holds information for column





    # Bound column as canidates    
    for votes in poll:
            candidates.append(votes[2]) #column index 
            
    # Create list of unique canidates
    nominee = {}
    for name in set(candidates):
        nominee.update({name: 0})
        
    # Loop through list to update dictionary values
    for votes in candidates:
        nominee[votes] += 1
    
    total_votes = sum(nominee.values())

    print("Election Results")
    print("--------------------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------------------")
    for delegates in nominee:
        #vote count for each nominee
        vote_count = nominee[delegates]
        
        #percent of votes obtained by each candidate 
        percent = round(float((vote_count/total_votes) * 100))
        
        print(f"{delegates}: {percent}.00% ({vote_count})")
    print("--------------------------------")
    # create an index to calculate winning percentage.
    if delegates in nominee:
        index = candidates.index(votes)
         #The winner of the election based on popular vote.
        ballots.append(percent)
        winning_percent = ballots.index(max(ballots))
        winner = candidates[winning_percent]
    #print(winner)
    print(f"Winner:  {winner}")
    print("--------------------------------")
    
    
    # 1) open a file for writing:
    f = open("poll.txt", "w")
    #2) replace all your print statements by print >>f, for example:
    # print "hello" becomes print >>f, "hello
    #3) close the file when you're done
    #f.close()
    print("REPRINT REPRINT REPRINT", file=f)
    print("Election Results", file=f)
    print("--------------------------------", file=f)
    print(f"Total Votes: {total_votes}", file=f)
    print("--------------------------------", file=f)
    for delegates in nominee:
        #vote count for each nominee
        vote_count = nominee[delegates]
        
        #percent of votes obtained by each candidate 
        percent = round(float((vote_count/total_votes) * 100))
        
        print(f"{delegates}: {percent}.00% ({vote_count})")
    print("--------------------------------", file=f)
    print(f"Winner:  {winner}", file=f)
    print("--------------------------------", file=f)
    f.close()