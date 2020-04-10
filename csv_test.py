import csv
import os

path = 'C:\\Users\\44779\\Desktop\\Python_tests\\test_data.txt'  # path is function of OS module - so import os module

..
def _convert_row():
    for row in my_list:
        # For row 0
        str1 = ''.join(row[0])  # Converting char to string
        temp_str1 = str1.split(',')  # splitting the string at ,
        r0 = temp_str1[0]  # printing first part of string

        # For row 1
        r1 = ''.join(row[1])

        # For row 2
        str2 = ''.join(row[2])  # list comprehension - converting CHAR to sting
        temp_str2 = float(str2)  # Converting string to float
        r2 = int(temp_str2)  # finally converting float to int
        print(r0, ",", r1, ",", r2)


with open(path, 'r') as f:  # reading file as read only
    reader = csv.reader(f)  # converting the text to read as csv - hence importing csv module
    next(reader)  # skip header
    my_list = list(reader)  # converting the csv as list
    print(_convert_row())
