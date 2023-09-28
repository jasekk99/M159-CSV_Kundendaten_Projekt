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

df = pd.read_csv('../CSV/export_Kunden_DE_E.csv', encoding = "utf-8", delimiter=";", encoding_errors='ignore')


def deleteZusatzColumns():
    columnsToIgnore  = []
    for x in range(100):
        if x==0:
            continue
        else:
            columnsToIgnore.append('Zusatz '+str(x))

    for x in columnsToIgnore:
        df.drop(x, inplace=True, axis=1)
        #print('✔  Dropped "'+x+'"')
    print('✔  Dropped 99 Columns')

def formattierung_Anrede():
    df['Anrede'] = df['Anrede'].str.lower()




deleteZusatzColumns()


time.sleep(2)

df.to_csv('test1.csv', sep=';', index=False, encoding='utf-8')
print(df.head(100))