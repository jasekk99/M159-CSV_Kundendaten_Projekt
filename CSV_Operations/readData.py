import pandas as pd
from time import sleep
import bcolors as b
import string
import re
from datetime import datetime
import numpy as np
from alive_progress import alive_bar
import random
import secrets

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
    #df.Titel = df.Titel.fillna('N/A')
    df.Titel = df.Titel.str.title()

def formattierung_Vorname():
    df['Vorname'] = df['Vorname'].str.replace(r'è', 'e', regex=True, flags=re.IGNORECASE)
    df['Vorname'] = df['Vorname'].str.replace(r'é', 'e', regex=True, flags=re.IGNORECASE)
    df['Vorname'] = df['Vorname'].str.replace(r'ê', 'e', regex=True, flags=re.IGNORECASE)
    df['Vorname'] = df['Vorname'].str.replace(r'ã', 'a', regex=True, flags=re.IGNORECASE)
    df['Vorname'] = df['Vorname'].str.replace(r'ř', 'r', regex=True, flags=re.IGNORECASE)
    df['Vorname'] = df['Vorname'].str.replace(r'ç', 'c', regex=True, flags=re.IGNORECASE)
    df['Vorname'] = df['Vorname'].str.replace(r'æ', 'ae', regex=True, flags=re.IGNORECASE)
    df['Vorname'] = df['Vorname'].str.replace(r'ø', 'o', regex=True, flags=re.IGNORECASE)
    df['Vorname'] = df['Vorname'].str.replace(r'å', 'a', regex=True, flags=re.IGNORECASE)
    df['Vorname'] = df['Vorname'].str.replace(r'í', 'i', regex=True, flags=re.IGNORECASE)
    df['Vorname'] = df['Vorname'].str.replace(r'ú', 'u', regex=True, flags=re.IGNORECASE)
    df['Vorname'] = df['Vorname'].str.replace(r'ù', 'u', regex=True, flags=re.IGNORECASE)
    df['Vorname'] = df['Vorname'].str.replace(r'û', 'u', regex=True, flags=re.IGNORECASE)
    df['Vorname'] = df['Vorname'].str.replace(r'ğ', 'g', regex=True, flags=re.IGNORECASE)
    df['Vorname'] = df['Vorname'].str.replace(r'ä', 'ae', regex=True, flags=re.IGNORECASE)
    df['Vorname'] = df['Vorname'].str.replace(r'ö', 'oe', regex=True, flags=re.IGNORECASE)
    df['Vorname'] = df['Vorname'].str.replace(r'ü', 'ue', regex=True, flags=re.IGNORECASE)
    df['Vorname'] = df['Vorname'].str.replace(r'ß', 'ss', regex=True, flags=re.IGNORECASE)
    df.Vorname = df.Vorname.str.title()

def formattierung_Nachname():
    df['Nachname'] = df['Nachname'].str.replace(r'è', 'e', regex=True, flags=re.IGNORECASE)
    df['Nachname'] = df['Nachname'].str.replace(r'é', 'e', regex=True, flags=re.IGNORECASE)
    df['Nachname'] = df['Nachname'].str.replace(r'ê', 'e', regex=True, flags=re.IGNORECASE)
    df['Nachname'] = df['Nachname'].str.replace(r'ã', 'a', regex=True, flags=re.IGNORECASE)
    df['Nachname'] = df['Nachname'].str.replace(r'ř', 'r', regex=True, flags=re.IGNORECASE)
    df['Nachname'] = df['Nachname'].str.replace(r'ç', 'c', regex=True, flags=re.IGNORECASE)
    df['Nachname'] = df['Nachname'].str.replace(r'æ', 'ae', regex=True, flags=re.IGNORECASE)
    df['Nachname'] = df['Nachname'].str.replace(r'ø', 'o', regex=True, flags=re.IGNORECASE)
    df['Nachname'] = df['Nachname'].str.replace(r'å', 'a', regex=True, flags=re.IGNORECASE)
    df['Nachname'] = df['Nachname'].str.replace(r'í', 'i', regex=True, flags=re.IGNORECASE)
    df['Nachname'] = df['Nachname'].str.replace(r'ú', 'u', regex=True, flags=re.IGNORECASE)
    df['Nachname'] = df['Nachname'].str.replace(r'ù', 'u', regex=True, flags=re.IGNORECASE)
    df['Nachname'] = df['Nachname'].str.replace(r'û', 'u', regex=True, flags=re.IGNORECASE)
    df['Nachname'] = df['Nachname'].str.replace(r'ğ', 'g', regex=True, flags=re.IGNORECASE)
    df['Nachname'] = df['Nachname'].str.replace(r'ä', 'ae', regex=True, flags=re.IGNORECASE)
    df['Nachname'] = df['Nachname'].str.replace(r'ö', 'oe', regex=True, flags=re.IGNORECASE)
    df['Nachname'] = df['Nachname'].str.replace(r'ü', 'ue', regex=True, flags=re.IGNORECASE)
    df['Nachname'] = df['Nachname'].str.replace(r'ß', 'ss', regex=True, flags=re.IGNORECASE)
    df['Titel'] = df['Nachname'].str.extract(r'(Dr\.)')
    df['Nachname'] = df['Nachname'].str.replace(r'(\bDr\.\s+\b)', '', regex=True)
    df.Nachname = df.Nachname.str.title()

def formattierung_Geburtsdatum():
    def is_valid_date(date_string):
        date_pattern = r'\d{2}-\d{2}-\d{4}'
        match = re.match(date_pattern, date_string)
        if match:
            try:
                date_obj = datetime.strptime(date_string, "%d-%m-%Y")
                formatted_date = date_obj.strftime("%d-%m-%Y")
                return formatted_date
            except ValueError:
                return date_string  # Keep if valid but with "dd-mm-yyyy" format
        else:
            return "Invalid Date"  # Keep as is if it doesn't match the pattern
        # Apply the function to the DataFrame and create a new column "valid_date"
    

    #df['Geburtsdatum'] = pd.to_datetime(df['Geburtsdatum'], format="mixed", errors='ignore')
    df['Geburtsdatum'] = df['Geburtsdatum'].str.replace('/','-')
    df['Geburtsdatum'] = df['Geburtsdatum'].str.replace('.','-')
    
    # Display the rows with valid dates
    df['Geburtsdatum'] = df['Geburtsdatum'].apply(is_valid_date)
    date_pattern = r'\b(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])-\d{4}\b'
    # Use boolean indexing to select rows where 'date_column' matches the pattern
    matched_dates = df[df['Geburtsdatum'].str.match(date_pattern)]

def formattierung_Strasse_Hausnummer():
    df['Strasse'] = df['Strasse'].str.replace(r'ß', 'ss', regex=True, flags=re.IGNORECASE)
    df['Strasse'] = df['Strasse'].str.replace(r'^', '', regex=True, flags=re.IGNORECASE)
    df.Strasse = df.Strasse.str.title()
    df['Hausnummer'].fillna(df['Strasse'], inplace=True)
    df['Strasse'] = df['Strasse'].str.replace('(?<=\d\s)[a-zA-Z]', '', regex=True)
    df['Strasse'] = df['Strasse'].str.replace('\d+', '', regex=True)
    df['Strasse'] = df['Strasse'].str.replace('\s[a-z].* [a-z]\s', '', regex=True)
    df['Hausnummer'] = df['Hausnummer'].str.replace('[a-zA-ZÄÖÜäöüß.-]+(?=\D*\d)', '', regex=True)
    df['Hausnummer'] = df['Hausnummer'].str.replace(' ', '', regex=True)
    df['Hausnummer'] = df['Hausnummer'].str.upper()

def formattierung_PLZ_Stadt():
    df.Stadt = df.Stadt.str.title()
    df['Postleitzahl'].fillna(df['Stadt'], inplace=True)
    df['Postleitzahl'] = df['Postleitzahl'].str.replace('[^0-9]', '', regex=True)
    df['Stadt'] = df['Stadt'].str.replace('\d', '', regex=True)
    df['Stadt'] = df['Stadt'].str.replace('^\s', '', regex=True)
    df['Stadt'] = df['Stadt'].str.replace(r'\bFeuersche\$D\b', 'Feuerscheid', regex=True)
    df['Stadt'] = df['Stadt'].str.replace(r'\bHeubaH\b', 'Heubach', regex=True)

def formattierung_Telefon(number):
    # Convert the float to a string
    number_str = str(number)
    
    # Remove all non-digit characters
    number_str = re.sub(r'[^+\d]', '', number_str)

    # Check if the number starts with "0" and add "+49" if it does
    if number_str.startswith('0'):
        number_str = "+49" + number_str[1:]

    # Add spaces for a consistent format
    #df['Mobil'] = df['Mobil'].str.replace('/\([^\d\n]*0[^\d\n]*\)/', '', regex=True)
    #df['Telefon'] = df['Telefon'].str.replace('^(?!.*\+).*$', '+', regex=True)
    formatted_number = re.sub(r'(\d{4})(\d+)', r'\1 \2', number_str)
    

    return formatted_number

def formattierung_Mobil(number):
    # Convert the float to a string
    number_str = str(number)
    
    # Remove all non-digit characters
    number_str = re.sub(r'[^+\d]', '', number_str)

    # Check if the number starts with "0" and add "+49" if it does
    if number_str.startswith('0'):
        number_str = "+49" + number_str[1:]

    # Add spaces for a consistent format
    #df['Mobil'] = df['Mobil'].str.replace('/\([^\d\n]*0[^\d\n]*\)/', '', regex=True)
    
    formatted_number = re.sub(r'(\d{4})(\d+)', r'\1 \2', number_str)
    

    return formatted_number

def formattierung_Email():
    df.EMail = df.EMail.str.lower()
    df['EMail'] = df['EMail'].str.replace(r'è', 'e', regex=True, flags=re.IGNORECASE)
    df['EMail'] = df['EMail'].str.replace(r'é', 'e', regex=True, flags=re.IGNORECASE)
    df['EMail'] = df['EMail'].str.replace(r'ê', 'e', regex=True, flags=re.IGNORECASE)
    df['EMail'] = df['EMail'].str.replace(r'ã', 'a', regex=True, flags=re.IGNORECASE)
    df['EMail'] = df['EMail'].str.replace(r'ř', 'r', regex=True, flags=re.IGNORECASE)
    df['EMail'] = df['EMail'].str.replace(r'ç', 'c', regex=True, flags=re.IGNORECASE)
    df['EMail'] = df['EMail'].str.replace(r'æ', 'ae', regex=True, flags=re.IGNORECASE)
    df['EMail'] = df['EMail'].str.replace(r'ø', 'o', regex=True, flags=re.IGNORECASE)
    df['EMail'] = df['EMail'].str.replace(r'å', 'a', regex=True, flags=re.IGNORECASE)
    df['EMail'] = df['EMail'].str.replace(r'í', 'i', regex=True, flags=re.IGNORECASE)
    df['EMail'] = df['EMail'].str.replace(r'ú', 'u', regex=True, flags=re.IGNORECASE)
    df['EMail'] = df['EMail'].str.replace(r'ù', 'u', regex=True, flags=re.IGNORECASE)
    df['EMail'] = df['EMail'].str.replace(r'û', 'u', regex=True, flags=re.IGNORECASE)
    df['EMail'] = df['EMail'].str.replace(r'ğ', 'g', regex=True, flags=re.IGNORECASE)
    df['EMail'] = df['EMail'].str.replace(r'ä', 'a', regex=True, flags=re.IGNORECASE)
    df['EMail'] = df['EMail'].str.replace(r'ö', 'o', regex=True, flags=re.IGNORECASE)
    df['EMail'] = df['EMail'].str.replace(r'ü', 'u', regex=True, flags=re.IGNORECASE)
    df['EMail'] = df['EMail'].str.replace(r'ß', 'ss', regex=True, flags=re.IGNORECASE)

def formattierung_Firma():
    df['Firma'] = df['Firma'].str.title()
    df['Firma'] = df['Firma'].str.replace(r'\bAg\b','AG', regex=True)
    df['Firma'] = df['Firma'].str.replace(r'\bKg\b','KG', regex=True)
    df['Firma'] = df['Firma'].str.replace(r'\bOhg\b','OHG', regex=True)
    df['Firma'] = df['Firma'].str.replace(r'\bUg\b','UG', regex=True)
    df['Firma'] = df['Firma'].str.replace(r'\bGbr\b','GbR', regex=True)
    df['Firma'] = df['Firma'].str.replace(r'\bKgaa\b','KGaA', regex=True)
    df['Firma'] = df['Firma'].str.replace(r'\bGmbh\b','GmbH', regex=True)

def formattierung_Bundesland():
    df['Bundesland'] = df['Bundesland'].str.replace(r'\bNieersachsen\b', 'Niedersachsen', regex=True)
    df['Bundesland'] = df['Bundesland'].str.replace(r'\bNiXdersachsen\b', 'Niedersachsen', regex=True)
    df['Bundesland'] = df['Bundesland'].str.replace(r'\bNordrhein-sestfalen\b', 'Nordrhein-Westfalen', regex=True)
    df['Bundesland'] = df['Bundesland'].str.replace(r'\bRandenburg\b', 'Brandenburg', regex=True)
    df['Bundesland'] = df['Bundesland'].str.replace(r'\bRheinland-Palz\b', 'Rheinland-Pfalz', regex=True)
    df['Bundesland'] = df['Bundesland'].str.replace(r'\bRheinand-Pfalz\b', 'Rheinland-Pfalz', regex=True)
    df['Bundesland'] = df['Bundesland'].str.replace(r'\bRheinland-Pfaz\b', 'Rheinland-Pfalz', regex=True)
    df['Bundesland'] = df['Bundesland'].str.replace(r'\bRheinland-Pfjlz\b', 'Rheinland-Pfalz', regex=True)
    df['Bundesland'] = df['Bundesland'].str.replace(r'\bRheinlnd-Pfalz\b', 'Rheinland-Pfalz', regex=True)
    df['Bundesland'] = df['Bundesland'].str.replace(r'\bSchleswig-Holtein\b', 'Schleswig-Holstein', regex=True)

def formattierung_Fax(number):
    # Convert the float to a string
    number_str = str(number)
    
    # Remove all non-digit characters
    number_str = re.sub(r'[^+\d]', '', number_str)

    # Check if the number starts with "0" and add "+49" if it does
    if number_str.startswith('0'):
        number_str = "+49" + number_str[1:]

    # Add spaces for a consistent format
    formatted_number = re.sub(r'(\d{4})(\d+)', r'\1 \2', number_str)
    

    return formatted_number

def formattierung_Aktiv():
    df['Aktiv'] = df['Aktiv'].str.lower()
    df['Aktiv'] = df['Aktiv'].str.replace(r'ja', 'True')
    df['Aktiv'] = df['Aktiv'].str.replace(r'nein', 'False')




with alive_bar(15, title='Bereinige CSV...', length=70) as bar:
    deleteZusatzColumns()
    bar()
    formattierung_Anrede()
    bar()
    formattierung_Titel()
    bar()
    formattierung_Vorname()
    bar()
    formattierung_Nachname()
    bar()
    formattierung_Geburtsdatum()
    bar()
    formattierung_Strasse_Hausnummer()
    bar()
    formattierung_PLZ_Stadt()
    bar()
    df['Telefon'] = df['Telefon'].apply(formattierung_Telefon)
    bar()
    df['Mobil'] = df['Mobil'].apply(formattierung_Mobil)
    bar()
    formattierung_Email()
    bar()
    formattierung_Firma()
    bar()
    formattierung_Bundesland()
    bar()
    df['Fax'] = df['Fax'].apply(formattierung_Fax)
    bar()
    formattierung_Aktiv()
    bar()



def formattierung_validator():

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
    
    #Nachname
    if df.Nachname.str.istitle().all() == True:
        print(b.OKGREEN+'✔  "Nachname" is Formatted correctly'+b.ENDC)
    else:
        print(b.FAIL+'✘  "Nachname" is  not Formatted correctly'+b.ENDC)

    #Geburtsdatum
    #if df['Geburtsdatum'].dt.date:
        #print(b.OKGREEN+'✔  "Geburtsdatum" is Formatted correctly'+b.ENDC)
    #else:
        #print(b.FAIL+'✘  "Geburtsdatum" is  not Formatted correctly'+b.ENDC)

    #Strasse
    if not df['Strasse'].str.contains(r'\d', regex=True).any():
        print(b.OKGREEN+'✔  "Strasse" is Formatted correctly'+b.ENDC)
    else:
        print(b.FAIL+'✘  "Strasse" is  not Formatted correctly'+b.ENDC)

    


formattierung_validator()




#Detailed/Readable version
df.to_csv('../CSV/Formattiert_export_Kunden_DE_E.csv', sep=';', index=False, encoding='utf-8')
 


#Preparation for AD Import [Reformatting column names+other adjustments
#df.rename(columns={'Vorname':'firstname', 'Nachname':'lastname'})
df['username'] = (df['Vorname'].str[0]+df['Nachname'].str[0:])
df['username'] = df['username'].str.lower()

mask = df['username'].duplicated(keep=False)
df.loc[mask, 'username'] += df.groupby('username').cumcount().add(1).astype(str)



pw_letters = string.ascii_letters
pw_digits = string.digits
#pw_special_chars = string.punctuation
pw_alphabet = pw_letters + pw_digits #+ pw_special_chars
pwd_length = 10
pwd = ''
pw_list = []
for a in range(len(df)):
    pwd=''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(pw_alphabet))
    pw_list.append(pwd)


#print(pw_list)

df['password'] = pw_list








#AD Import Version (Not intended to be opened and used for references)
df.to_csv('../CSV/output.csv', sep=';', index=False, encoding='utf-8')