#PyPoll python-challenge

#Set Dependencies
import os
import csv

#Establish path the csv file
csvpath = os.path.join('Resources', 'election_data.csv')

#print(csvpath)

def total_votes(data):
	total_votes = 0	
	for row in data:
		total_votes += 1

	return total_votes
def candidates(data): 
	#candidates = row[2] for row[2] in data if row[2] not in candidates
	candidates = []
	for row in data:
		if row[2] not in candidates:
			candidates.append(row[2])
	return candidates



#Read the csv file
with open(csvpath, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')

	header = next(csvreader)

	election_data = list(csvreader)
	

	total_votes_results = total_votes(election_data)
	candidates_results = candidates(election_data)
	


print(total_votes_results)
print(candidates_results)
