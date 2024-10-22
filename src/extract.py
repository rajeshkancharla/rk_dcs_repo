# import packages
import pandas as pd # type: ignore
import numpy as np


# define variables
column_headers = ['FirstName', 'LastName', 'Company', 'BirthDate', 'Salary', 'Address', 'Suburb', 'State', 'Post', 'Phone', 'Mobile', 'Email']
separator = '|'
filename = 'member-data.csv'
referenceDate = '20240301'

# define modules
def read_file(filename:str, separator:str, column_names:str) -> pd.DataFrame:
    df = pd.read_csv(filename, sep = separator, names = column_names)
    return df

def process_date(df: pd.DataFrame) -> pd.DataFrame:
    df['BirthDate'] = df['BirthDate'].astype('Int64').astype(str).str.zfill(8)
    df['BirthDate'] = pd.to_datetime(df['BirthDate'], format='%d%m%Y', errors = 'coerce')
    df['BirthDate'] = df['BirthDate'].dt.strftime('%d/%m/%Y')
    return df

def process_string(df: pd.DataFrame) -> pd.DataFrame:
    df['FirstName'] = df['FirstName'].str.strip()
    df['LastName'] = df['LastName'].str.strip()
    df['FullName'] = df['FirstName'] + ' ' + df['LastName']
    return df

def process_number(df: pd.DataFrame) -> pd.DataFrame:
    df['Salary'] = df["Salary"].map('${:,}'.format)
    return df

def calculate_age(df: pd.DataFrame, referenceDate: str) -> pd.DataFrame:
    refDate = referenceDate.zfill(8)
    refDate = pd.to_datetime(refDate, format='%Y%m%d', errors = 'coerce')
    df["DaysDiff"] = refDate - pd.to_datetime(df['BirthDate'], format='%d/%m/%Y')
    df["Age"] = df["DaysDiff"].dt.days.astype("Int16") // 365
    df.drop('DaysDiff', axis=1, inplace=True)
    return df

def calculate_salarybucket(df: pd.DataFrame) -> pd.DataFrame:    
    df['SalaryBucket'] = np.where(df['Salary'] < 50000, 'A', '')
    df['SalaryBucket'] = np.where(df['Salary'] >= 100000, 'C', 'B')
    return df

df_file = read_file(filename = filename, separator = separator, column_names = column_headers)

df_file = process_date(df_file)

df_file = process_string(df_file)

df_file = calculate_salarybucket(df_file)

df_file = process_number(df_file)

df_file = calculate_age(df_file, referenceDate=referenceDate)

df_file = df_file.drop(columns=['FirstName','LastName'], axis=1)

#print(df_file.to_string())

df_file.to_json('enriched_data.json', orient='records', lines=True)