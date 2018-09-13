#establish imports
import os
import csv


#set csv path 
csvpath = os.path.join('Resources', 'budget_data.csv') 

#print(csvpath)


#Define functions that will use budget_Data
def months_count(data):
		return len(data)
def net_profit_loss(data):
	total = 0.0
	for row in data:
		total += float(row[1])
	return total
def avg_profitLoss(data):
	total = 0.0
	for row in data:
		total += float(row[1])
		totalMonths = len(data)
	return total/totalMonths
def max_profitIncrease(data):
	maxProfit = max(data, key=lambda row: float(row[1]))
	return maxProfit

def min_profitDecrease(data):
	minProfit = min(data, key=lambda row: float(row[1]))
	return minProfit
	
	


#Average change between months function
#def ave_monthly_change():
	#'''
	#DOCSTRING: calculates the average change between months
	#INPUT: budgetData
	#OUTPUT: Average Change between months
	#'''
	#return 
#Read the csv file
with open(csvpath, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')

	header = next(csvreader)

	#Count the number of months in data
	budgetData = list(csvreader)
	
	#profitLossData = 




	#Data Results
	months_count_result = months_count(budgetData)
	total_profitLoss_result = net_profit_loss(budgetData)
	avg_profitLoss_result = total_profitLoss_result/months_count_result
	greatest_profitIncrease_result = max_profitIncrease(budgetData)
	greatest_profitDecrease_result = min_profitDecrease(budgetData)

#Print results

	print(months_count_result)
	print(total_profitLoss_result)
	print(avg_profitLoss_result)
	print(greatest_profitIncrease_result)
	print(greatest_profitDecrease_result)
#print(f'Total: ${}')
#print(f'Average Change: ${avg_monthly_change_result}')
#print(f'Greatest Increase in Profits: {} {}')
#print(f'Greatest Decrease in PRofits: {} {}')	

# Set variable for output file
output_file = os.path.join("web_final.csv")


#  Open the output file
#with open(output_file, "w", newline="") as datafile:
#    writer = csv.writer(datafile)
#
#    # Write the header row
#    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
#                     "Percent of Reviews", "Length of Course"])
#
#    # Write in zipped rows
#    writer.writerows(cleaned_csv)
	


	


	