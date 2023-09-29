import pandas as pd
import os
import time
import csv
import numpy as np

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
    df.Anrede = df.Anrede.str.lower()

def formattierung_Titel():
    #Titel is the name of the column and title is the name of the capitalization function in pandas
    df.Titel = df.Titel.str.title()




deleteZusatzColumns()
formattierung_Anrede()
formattierung_Titel()

def formattierung_validator():
    #Anrede
    if df.Anrede.str.islower().all() == True:
        print('✔  "Anrede" is Formatted correctly')

    #Titel
    if df.Titel.str.istitle().all() == True:
        print('✔  "Titel" is Formatted correctly')

formattierung_validator()


df.to_csv('../CSV/output.csv', sep=';', index=False, encoding='utf-8')
#print(df.head(100))