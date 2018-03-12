#Declaring the import os, CSV, operator, collection with counter
import os
import csv
import operator
from collections import Counter

#Define PyPoll_result function
def Pypoll_result():
    count = 0
    #Looping listdir of raw_data of cvs file
    for fname in os.listdir('raw_data'):
        print(fname)
        count = count + 1
        inputfolder = 'raw_data' + '/' + fname
        output_file = 'analysis' + '/' + \
            'election_analysis_' + str(count) + '.txt'
        output_analysis = ''
        print(inputfolder)
        #Created first list_candidate list which read data from Reader
        list_candidate = []
        #Created second unique_list_candidate list which will keep value of just candidate column
        unique_list_candidate = []
        candidate_name = ''
        #Opening input CSV file
        with open(inputfolder) as csvfile:
            reader = csv.DictReader(csvfile)
            list_candidate = list(reader)
            #total count of entire row
            total_count = len(list_candidate)
            for x in list_candidate:
                unique_list_candidate.append(x[('Candidate')])
            #Looping through Counter dictionary for  listunique_list_candidate list
            #inside Loop getting Candidate name, and how much votes each candidate have received
            #What is percentage of each count
            #Who is winner with highest count
            for k, y in Counter(unique_list_candidate).items():
                key = k
                value = y
                percentage = (value/total_count)*100
                print(key + " " + str(value) + " " + str(percentage))
                candidate_name = candidate_name + \
                    (f"{key} : {value} {percentage}%\n")
            maxvalue = max(Counter(unique_list_candidate).items(),
                           key=operator.itemgetter(1))[0]
            print('Winner is ' + maxvalue)
            output_analysis = (f"\nElection Results\n"
                               f"----------------------------\n"
                               f"Total Votes: {total_count}\n"
                               f"----------------------------\n")
            maxvalue_result = (f"\n--------------------------\n"
                               f"winner: {maxvalue}\n")
           #Wrote Election to output file and saved output file in output folder
            with open(output_file, "w") as txt_file:
                    txt_file.write(output_analysis +
                                   candidate_name + maxvalue_result)
    return
#Call function 
Pypoll_result()
