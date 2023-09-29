import pandas as pd
#import os
#import time
#import numpy as np
import bcolors as b
import string

df = pd.read_csv('../CSV/export_Kunden_DE_E.csv', encoding = "utf-8", delimiter=";", encoding_errors='ignore')

columnsToIgnore  = []
def deleteZusatzColumns():
    
    for x in range(100):
        if x==0:
            continue
        else:
            columnsToIgnore.append('Zusatz '+str(x))

    for x in columnsToIgnore:
        df.drop(x, inplace=True, axis=1)
        #print('✔  Dropped "'+x+'"')

def formattierung_Anrede():
    df.Anrede = df.Anrede.str.lower()

def formattierung_Titel():
    #Titel is the name of the column and title is the name of the capitalization function in pandas
    df.Titel = df.Titel.str.title()

def formattierung_Vorname():
    df.Vorname = df.Vorname.str.title()




deleteZusatzColumns()
formattierung_Anrede()
formattierung_Titel()
formattierung_Vorname()



def formattierung_validator():
    special_chars = 'è|È|é|É|ê|Ê|ã|Ã|ř|Ř|ç|Ç|Æ|æ|Ø|ø|Å|å|í|Í'


    #Zusatz-Columns
    errors_columnsToIgnore = []
    for x in columnsToIgnore:
        if x in df.columns:
            errors_columnsToIgnore.append('True')
        else:
            errors_columnsToIgnore.append('False')
    
    if 'True' not in errors_columnsToIgnore:
        print(b.OKBLUE+'✔  Dropped 99 Columns'+b.ENDC)
    else:
        print(b.FAIL+'✘  Error Dropping 99 Columns'+b.ENDC)

    #Anrede
    if df.Anrede.str.islower().all() == True:
        print(b.OKGREEN+'✔  "Anrede" is Formatted correctly'+b.ENDC)
    else:
        print(b.FAIL+'✘  "Anrede" is  not Formatted correctly'+b.ENDC)

    #Titel
    if df.Titel.str.istitle().all() == True:
        print(b.OKGREEN+'✔  "Titel" is Formatted correctly'+b.ENDC)
    else:
        print(b.FAIL+'✘  "Titel" is  not Formatted correctly'+b.ENDC)

    #Vorname
    if df.Vorname.str.istitle().all() == True:
        print(b.OKGREEN+'✔  "Vorname" is Formatted correctly'+b.ENDC)
    else:
        print(b.FAIL+'✘  "Vorname" is  not Formatted correctly'+b.ENDC)

    # I HAVE BEEN STUCK ON THIS PART FOR AN HOUR I CANT ANYMORE PLEASE SEND HELP. 🤓"pandas.errors.IndexingError: Unalignable boolean Series provided as indexer (index of the boolean Series and of the indexed object do not match)"🤓
    #contains_special_chars = df[df.Titel.str.contains(special_chars)]
    #print (contains_special_chars)


formattierung_validator()


df.to_csv('../CSV/output.csv', sep=';', index=False, encoding='utf-8')
#print(df.head(100))