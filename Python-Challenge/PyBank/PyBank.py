import os
import csv

# Specify the file to write to
# Specify the file to write to
csvpath=os.path.join('..', '..', 'gt-atl-data-pt-06-2020-u-c', 'DataViz-Content', '03-Python', 'Homework', 'Instructions', 'PyBank', 'Resources', 'budget_data.csv')

                           

# Open the file using path. Specify the variable to hold the contents
with open(csvpath) as csvfile:
    # Initialize csv.reader
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip Header on CSV and read next row              
    csvheader = next(csvreader)
    #print(f"Header: {csvheader}")
                           
    # intitialize list
    month = []
    monthly_change = [] 
    revenue = []  
    total_change = [] 
        
    #Read each row of data then get the length for total months
    data = list(csvreader)
    total_months = len(data)
    #print(total_months)
        
    #profit/loss = "  " = "  " initialize 
    pl = total_change = average_change = 0
    # The column will be profit/loss
    for col in data: 
        # append dates to match to greatest decrease and increase
        month.append(col[0])
                           
        # column profit loss col[1]
        values = col[1]
            
        # add values in list of revenue
        revenue.append(values)
                           
        # Turn values appeneded into revenue to integer for total sum
        # Note to self, make sure its out of the loop along with calculations after!
        total = sum((int(integral) for integral in revenue))
        #print(total)
        
        # p will serve as my row                   
        p = 0 
        # offset revenue values by one to calculate change
        for p in range(len(revenue) - 1): 
            pl = int(revenue[p+1]) - int(revenue[p])
            monthly_change.append(pl)
            
            # average change round to 100th
            total_change = sum(monthly_change)
            average_change = round(total_change/(len(monthly_change)), 2)
            #print(total_change)
            #print(average_change)
        
            #Greatest Increase
            profit_increase = max(monthly_change)
            #print(profit_increase)
            q = monthly_change.index(profit_increase)
            month_increase = month[q+1]
        
            #Greatest Decrease
            profit_decrease = min(monthly_change)
            #print(profit_decrease)
            r = monthly_change.index(profit_decrease)
            month_decrease = month[r+1]
        
print(f'Financial Analysis'+'\n')
print(f'----------------------------'+'\n')

print("Total number of months: " + str(total_months))

print("Total Revenue in period: $ " + str(total))
      
print("Average monthly change in Revenue : $" + str(average_change))

print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")

print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")

    
# 1) open a file for writing:
f = open("bank.txt", "w")
#2) replace all your print statements by print >>f, for example:
# print "hello" becomes print >>f, "hello
#3) close the file when you're done
#f.close()
print("REPRINT REPRINT REPRINT", file=f)
print(f'Financial Analysis'+'\n', file=f)
print(f'----------------------------'+'\n', file=f)

print("Total number of months: " + str(total_months), file=f)

print("Total Revenue in period: $ " + str(total), file=f)
      
print("Average monthly change in Revenue : $" + str(average_change), file=f)

print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})", file=f)

print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})", file=f)
f.close()       

            