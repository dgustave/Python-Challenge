import os
import csv
from datetime import datetime

input_file = 'employee_archive.csv'
output_file = 'employee_archive_clean.csv'

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# declare lists of 10 and intialize before paths
emp_id, full_name, first_name, last_name, dob, dob_modified, ssn, ssn_filtered, state, state_abbrev = ([]) * 10

# Specify the file to write to
csvpath=os.path.join('..', '..','..','..', 'gt-atl-data-pt-06-2020-u-c', 'DataViz-Content', '03-Python', 'ExtraContent', 'Homework', 'Instructions', 'PyBoss',  'employee_data.csv', input_file)
clean_csvpath=os.path.join('clean_data', output_file)

# pull data from unformatted csv files and load lists
with open(csv_path, 'r', newline= '') as employee_data:
    archive = csv.reader(employee_data)

    # skip headers before loading lists
    next(reader)
    # gather original data for modification and load into lists
    for col in archive:
        emp_id.append(row[0])
        full_name.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        state.append(row[4])
        
# formatting new list 
for e in range(len(full_name)):
    
    # Use a single space to split first/last name
    split_name = full_name[i].split(" ")
    first_name.append(split_name[0])
    last_name.append(split_name[1])
    
    

