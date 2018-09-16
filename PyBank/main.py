#establish imports
import os
import csv
import datetime

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
	total_profitLoss_result = '${:,.2f}'.format(net_profit_loss(budgetData))
	#avg_profitLoss_result = total_profitLoss_result/months_count_result
	greatest_profitIncrease_result = max_profitIncrease(budgetData)
	greatest_profitDecrease_result = min_profitDecrease(budgetData)

#Print results
print("\nFinacial Analysis!!!\n___________________________\n")
print(f'Total Month: {months_count_result}')
print(f'Total : {total_profitLoss_result}')
print(f'Greatest Increase in Profits: {greatest_profitIncrease_result}')
print(f'Greatest Decrease in Profits: {greatest_profitDecrease_result}')

#print(f'Total: ${}')
#print(f'Average Change: ${avg_monthly_change_result}')
#print(f'Greatest Increase in Profits: {} {}')
#print(f'Greatest Decrease in PRofits: {} {}')	

# Set variable for output file
output_file = os.path.join("PyBank_results.txt")


#  Open the output file
with open(output_file, "w", newline="") as datafile:
	writer = csv.writer(datafile)

    # Write the header row
    #write results to txt file
	writer.writerow(["Finacial Analysis \n  -----------------------------"])
	writer.writerow(f'Total Months: {greatest_profitIncrease_result}')
	writer.writerow(f'Average Change: {greatest_profitIncrease_result}')
	writer.writerow(f'Greatest Increase: {greatest_profitIncrease_result}')
	writer.writerow(f'Greatest Decrease: {greatest_profitIncrease_result}')
#    # Write in zipped rows
#    writer.writerows(cleaned_csv)
	


	


	