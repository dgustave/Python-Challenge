import os
import csv

# Specify the file to write to
budget_data = os.path.join(('..', 'Resources', 'budget_data.csv')
total_months = [] 

# Open the file using path. Specify the variable to hold the contents
with open(budget_data, 'r') as csvfile:
    # Initialize csv.reader
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip Header on CSV               
cvsheader = next(csvreader) 
        # intitialize variables 

for col in csvreader:
    for row in csvreader:
            total_months = total_months + 1
            print(total_months)
                    
            