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

#Set function to find total number of votes for Khan
def total_khan_votes(data):
	total_khan_votes = 0
	for row in data:
		if row[2] == 'Khan':
			total_khan_votes += 1
	return total_khan_votes
#Set function to find total number of votes for Khan
def total_correy_votes(data):
	total_correy_votes = 0
	for row in data:
		if row[2] == 'Correy':
			total_correy_votes += 1
	return total_correy_votes

def total_li_votes(data):
	total_li_votes = 0
	for row in data:
		if row[2] == 'Li':
			total_li_votes += 1
	return total_li_votes

def total_otooley_votes(data):
	total_otooley_votes = 0
	for row in data:
		if row[2] == "O'Tooley":
			total_otooley_votes += 1
	return total_otooley_votes



#Read the csv file
with open(csvpath, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	#skip the header row
	header = next(csvreader)
	#set reader as election data
	election_data = list(csvreader)
	

	#Calculate the total number of votes in data 
	total_votes_results = total_votes(election_data)
	#Get results of the list of candidates that recieved a vote
	candidates_results = candidates(election_data)

	#Get results of the function that calculates the total of number of votes for candidata (Khan, Correy, Li, O'Tooley)
	khan_votes_results = total_khan_votes(election_data)
	correy_votes_results = total_correy_votes(election_data)
	li_votes_results = total_li_votes(election_data)
	otooley_votes_results = total_otooley_votes(election_data)

	#Get results of candidate vote percentages 
	khan_votes_percentatge = '{:.0}%'.format((khan_votes_results / total_votes_results) * 100)
	correy_votes_percentatge = '{:.0}%'.format((correy_votes_results / total_votes_results) * 100)
	li_votes_percentatge = '{:.0}%'.format((li_votes_results / total_votes_results) * 100)
	otooley_votes_percentatge = '{:.0}%'.format((otooley_votes_results / total_votes_results) * 100)

	vote_totals_list = [khan_votes_results, correy_votes_results, li_votes_results, otooley_votes_results]
	#print(percentage_votes_list)
	#print(type(percentage_votes_list))
	#Determing winner
	winner = None
	if khan_votes_results == max(vote_totals_list):
		winner = "Khan"
	elif correy_votes_results == max(vote_totals_list):
		winner = "Correry"
	elif li_votes_results == max(vote_totals_list):
		winner = "Li"
	else:
		winner = "O'Tooley"


print("\nElection Results" )
print(f'_________________________________\nTotal Votes: {total_votes_results}\n_________________________________')
print(f'{candidates_results[0]}: {khan_votes_percentatge} ({khan_votes_results})')
print(f'{candidates_results[1]}: {correy_votes_percentatge} ({correy_votes_results})')
print(f'{candidates_results[2]}: {li_votes_percentatge} ({li_votes_results})')
print(f'{candidates_results[3]}: {otooley_votes_percentatge} ({otooley_votes_results})')
print(f'_________________________________\nWinner: {winner}\n_________________________________')



output_file = os.path.join("PyBank_results.txt")


#  Open the output file
with open(output_file, "w", newline="") as datafile:
	writer = csv.writer(datafile)
#
#    # Write the header row
	writer.writerow(["Election Results"])
	writer.writerow([f"_________________________________\nTotal Votes: total_votes_results\n_________________________________"])
	writer.writerow([f"{candidates_results[0]}: {khan_votes_percentatge} ({khan_votes_results})"])
	writer.writerow([f"{candidates_results[1]}: {correy_votes_percentatge} ({correy_votes_results})"])
	writer.writerow([f"{candidates_results[2]}: {li_votes_percentatge} ({li_votes_results})"])
	writer.writerow([f"{candidates_results[3]}: {otooley_votes_percentatge} ({otooley_votes_results})"])
	writer.writerow([f"_________________________________\nWinner: {winner}\n_________________________________"])


	#writer.writerow(greatest_profitIncrease_result)


#print(khan_votes_results)	
#print("{0:.0%}".format(khan_votes_percentatge))
#print(correy_votes_results)	
#print("{0:.0%}".format(correy_votes_percentatge))
#print(winner)


#Export a text file with the results
#Create txt file variable

#output_file = os.join.path("PyPoll_Results")