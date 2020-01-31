import csv
import os

path = 'C:\\Users\\44779\\Desktop\\Python_tests\\test_data.txt'


def _convert_row():
    for row in my_list:
        # For row 0
        str1 = ''.join(row[0])
        temp_str1 = str1.split(',')
        r0 = temp_str1[0]

        # For row 1
        r1 = ''.join(row[1])

        # For row 2
        str2 = ''.join(row[2])
        temp_str2 = float(str2)
        r2 = int(temp_str2)
        print(r0, ",", r1, ",", r2)


with open(path, 'r') as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    my_list = list(reader)
    print(_convert_row())
