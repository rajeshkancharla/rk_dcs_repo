import pandas as pd
import numpy as np
from pymongo import MongoClient

class FileDataClass:

    def __init__(self, file_path) -> None:
        """
        This is to instantiate the objects of this class
        """
        self.file_path = file_path
        self.address_details = self.Address()
    
    def create_df(self: str) -> pd.DataFrame:
        """
        This function is to create the Pandas dataframe by reading from the file
        """
        column_headers = ['FirstName', 'LastName', 'Company', 'BirthDate', 'Salary', 'Address', 'Suburb', 'State', 'Post', 'Phone', 'Mobile', 'Email']
        df = pd.read_csv(self.file_path, sep='|', names=column_headers)
        return df
    
    def process_number(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        This function is to transform the Salary field from a floating point value to a currency format with $ symbol along with commas and decimals
        """
        df['Salary'] = df["Salary"].map('${:,}'.format)
        return df
    
    def process_date(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        This function is to transform the BirthDate from DDMMYYYY to DD/MM/YYYY format
        """
        df['BirthDate'] = df['BirthDate'].astype('Int64').astype(str).str.zfill(8)
        df['BirthDate'] = pd.to_datetime(df['BirthDate'], format='%d%m%Y', errors = 'coerce')
        df['BirthDate'] = df['BirthDate'].dt.strftime('%d/%m/%Y')
        return df

    def process_string(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        This function is to cleanse the FirstName and LastName fields. And create a new field called FullName
        """
        df['FirstName'] = df['FirstName'].str.strip()
        df['LastName'] = df['LastName'].str.strip()
        df['FullName'] = df['FirstName'] + ' ' + df['LastName']
        return df

    def calculate_age(self, df: pd.DataFrame, referenceDate: str) -> pd.DataFrame:
        """
        This function is to calculate the Age based on the BirthDate and a static given date in requirement
        """
        refDate = referenceDate.zfill(8)
        refDate = pd.to_datetime(refDate, format='%Y%m%d', errors = 'coerce')
        df["DaysDiff"] = refDate - pd.to_datetime(df['BirthDate'], format='%d/%m/%Y')
        df["Age"] = df["DaysDiff"].dt.days.astype("Int16") // 365
        df.drop('DaysDiff', axis=1, inplace=True)
        return df

    def calculate_salarybucket(self, df: pd.DataFrame) -> pd.DataFrame: 
        """
        This function is to calculate the Salary Bucket as A, B, C according to the ranges provided in requirement
        """   
        df['SalaryBucket'] = np.where(df['Salary'] < 50000, 'A', '')
        df['SalaryBucket'] = np.where(df['Salary'] >= 100000, 'C', 'B')
        return df
    
    class Address:

        def __init__(self) -> None:
            pass

        def nested_address(self, df: pd.DataFrame):
            self.address_details = {}

            df['AddressDetails'] = df.apply(lambda row: {
                'Address': row['Address'],
                'Suburb': row['Suburb'],
                'State': row['State'],
                'PostCode': row['Post']
            }, axis=1)

            return df


