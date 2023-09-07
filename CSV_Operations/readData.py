import pandas as pd
import os
import time
import chardet
import glob
import csv
import numpy as np

"""
print("File".ljust(45), "Encoding")
for filename in glob.glob('../CSV/*.csv'):
    with open(filename, 'rb') as rawdata:
        result = chardet.detect(rawdata.read())
    print(filename.ljust(45), result['encoding'])
"""

columnsToIgnore = []

for x in range(99):
    if x==0:
        continue
    else:
        columnsToIgnore.append('Zusatz '+str(x))


with open('../CSV/export_Kunden_DE_E.csv') as csv_file:
 
    # creating an object of csv reader
    # with the delimiter as ,
    csv_reader = csv.reader(csv_file, delimiter = ';')
 
    # list to store the names of columns
    list_of_column_names = []
 
    # loop to iterate through the rows of csv
    for row in csv_reader:
 
        # adding the first row
        list_of_column_names.append(row)
 
        # breaking the loop after the
        # first iteration itself
        break


print(list_of_column_names[0])

df = pd.read_csv('../CSV/export_Kunden_DE_E.csv', encoding = "MacRoman", delimiter=";")
#print(df.to_string())