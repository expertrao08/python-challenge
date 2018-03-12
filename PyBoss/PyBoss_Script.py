#import CSV, os Datetime, itertools
import csv
import os
from datetime import datetime
import itertools

# Created Dictionary of states with abbreviations

us_state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}
count = 0
#Getting raw data file name 
for fname in os.listdir('raw_data'):
    inputfolder = 'raw_data' + '/' + fname
    print(fname)
    count = count + 1
    output_file = 'output' + '/' + \
        'output_employee_data' + str(count) + '.csv'
    print(output_file)
    #Declaring all List of column
    Emp_ID=[]
    Name = []
    First_Name = []
    Last_Name = []
    DOB = []
    SSN = []
    State = []
    #Opening Rawdata CSV file
    with open(inputfolder) as csvfile:
        reader = csv.DictReader(csvfile)
        #Looping through Reader getting value adding them in List
        for row in reader:
            #Employee ID List
            Emp_ID = Emp_ID + [row["Emp ID"]]
            #split Name into two Array, adding them in each List
            Emp_Name = row["Name"].split(" ")
            First_Name = First_Name + [Emp_Name[0]]
            Last_Name = Last_Name + [Emp_Name[1]]
            #Using DateTime function making new format - mm/dd/yyyy
            newFormat_DOB = datetime.strptime(row["DOB"], "%Y-%m-%d")
            newFormat_DOB = newFormat_DOB.strftime('%m/%d/%Y')
            DOB = DOB + [newFormat_DOB]
            #Whole SSN split them 3 different array and join them as one adding in list
            emp_SSN = list(row['SSN'])
            emp_SSN[0:3] = ("*", "*", "*")
            emp_SSN[4:6] = ("*","*")
            new_emp_SSN = "".join(emp_SSN)
            SSN = SSN + [new_emp_SSN]
            #Using US State Abbrev dictory, paasing them State Key column and getting value as abbrev
            State_abbrev = us_state_abbrev[row["State"]]
            State = State + [State_abbrev]
    #using itertools of python merging All list into one one which new_emp_List
    new_emp_List = itertools.chain(zip(Emp_ID, First_Name, Last_Name, DOB, SSN, State))
    #Writing to output file
    print('New File ' + output_file)
    with open(output_file, "w", newline="") as datafile:
        writer = csv.writer(datafile)
        writer.writerow(["Emp ID", "First Name", "Last Name",
                     "DOB", "SSN", "State"])
        writer.writerows(new_emp_List)
