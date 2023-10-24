import pandas as pd
from time import sleep
import bcolors as b
import string
import re
from datetime import datetime
import numpy as np
from alive_progress import alive_bar

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

def formattierung_Telefon(number):
    # Convert the float to a string
    number_str = str(number)
    
    # Remove all non-digit characters
    number_str = re.sub(r'[^+\d]', '', number_str)

    # Check if the number starts with "0" and add "+49" if it does
    if number_str.startswith('0'):
        number_str = "+49" + number_str[1:]

    # Add spaces for a consistent format
    df['Mobil'] = df['Mobil'].str.replace('/\([^\d\n]*0[^\d\n]*\)/', '', regex=True)
    df['Telefon'] = df['Telefon'].str.replace('^(?!.*\+).*$', '+', regex=True)
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



print()
with alive_bar(10, title='Bereinige CSV...', length=70) as bar:
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


df.to_csv('../CSV/output.csv', sep=';', index=False, encoding='utf-8')
#print(df.head(100))