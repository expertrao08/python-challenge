#Pybank python-challenge
import csv
import os

data_path = "raw_data/"
listoffiles = ['budget_data_1.csv','budget_data_2.csv']

for file in listoffiles:
    file_obj = data_path + file
    data_dict_list = {}
    with open(file_obj) as csvfile:
        reader = csv.DictReader(csvfile)
        revenue = 0
        rev_diff = 0
        for row in reader:
            rev_diff = rev_diff + int(row[('Revenue')])-revenue
            revenue = int(row[('Revenue')])
            data_dict_list[row[('Date')]] = int(rev_diff)
    print(len(data_dict_list))
