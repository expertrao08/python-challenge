#Pybank python-challenge

#import CSV, OS and Operator
import csv
import os
import operator

#declaring variable for output file folder and raw data path folder
data_path = "raw_data/"
output_path = "output_data/"
outputfile = "analysis_report_"

#Creating listoffiles of raw data 
listoffiles = ['budget_data_1.csv','budget_data_2.csv']
count=0

#Looping through list of files and based on count of for loop creating output file
for file in listoffiles:
    file_obj = data_path + file
    count = count + 1
    file_output = output_path + outputfile + str(count) +".txt"
    print(file_output)

    #creating function call pybankresult which take two Parameter like file object and string name of output file
    def pybankresult(file_obj, file_output):
        #Opening raw data file 
        with open(file_obj) as csvfile:
            reader = csv.DictReader(csvfile)
            #declaring varaibles of month, revenue, revenue change
            revenue = 0
            rev_diff = 0
            total_revenue = 0
            sum_revenue_change=0
            total_month = 0
            avg_revenue = 0
            data_dict_list = {}
            #Looping through csv reader and calculating total revenue and rev_diff, 
            # adding them in dictionary with key of data and value as revenue change
            for row in reader:
                total_revenue = total_revenue + int(row[('Revenue')])
                rev_diff = int(row[('Revenue')])-revenue
                revenue = int(row[('Revenue')])
                data_dict_list[row[('Date')]] = int(rev_diff)
            
            #Looping through dictionary and calcuting sum of revenue change
            #using operator import found which max value and got key of that value
            #using key found out which value from dictionary
            #calulated Average of revenue divided by total month
            for k, v in data_dict_list.items():
                total_month = total_month + 1
                sum_revenue_change = sum_revenue_change + v

            maxkey = max(data_dict_list.items(), key=operator.itemgetter(1))[0]
            minkey = min(data_dict_list.items(), key=operator.itemgetter(1))[0]

            maxvalue = data_dict_list[maxkey]
            minvalue = data_dict_list[minkey]
            avg_revenue = (sum_revenue_change/total_month)
            #created String variable as analysis report 
            analysis_report = (f"\nFinancial Analysis\n"
                               f"----------------------------\n"
                               f"Total Months: ${total_month}\n"
                               f"Total Revenue: ${total_revenue}\n"
                               f"Average Revenue Change: ${avg_revenue}\n"
                               f"Greatest Increase in Revenue: {maxkey} (${maxvalue})\n"
                               f"Greatest Decrease in Revenue: {minkey} (${minvalue})\n")
            print(analysis_report)
            
            #based on input parameter created text file and 
            # wrote analysis report value in output file
            with open(file_output, "w") as txt_file:
                txt_file.write(analysis_report)
            return

    pybankresult(file_obj, file_output)