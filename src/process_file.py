import pandas as pd
import numpy as np

class FileDataClass:

    def __init__(self, file_path) -> None:
        self.file_path = file_path
    
    def create_df(self: str) -> pd.DataFrame:
        column_headers = ['FirstName', 'LastName', 'Company', 'BirthDate', 'Salary', 'Address', 'Suburb', 'State', 'Post', 'Phone', 'Mobile', 'Email']
        df = pd.read_csv(self.file_path, sep='|', names=column_headers)
        return df
    
    def process_number(self, df: pd.DataFrame) -> pd.DataFrame:
        df['Salary'] = df["Salary"].map('${:,}'.format)
        return df
    
    def process_date(self, df: pd.DataFrame) -> pd.DataFrame:
        df['BirthDate'] = df['BirthDate'].astype('Int64').astype(str).str.zfill(8)
        df['BirthDate'] = pd.to_datetime(df['BirthDate'], format='%d%m%Y', errors = 'coerce')
        df['BirthDate'] = df['BirthDate'].dt.strftime('%d/%m/%Y')
        return df

    def process_string(self, df: pd.DataFrame) -> pd.DataFrame:
        df['FirstName'] = df['FirstName'].str.strip()
        df['LastName'] = df['LastName'].str.strip()
        df['FullName'] = df['FirstName'] + ' ' + df['LastName']
        return df

    def calculate_age(self, df: pd.DataFrame, referenceDate: str) -> pd.DataFrame:
        refDate = referenceDate.zfill(8)
        refDate = pd.to_datetime(refDate, format='%Y%m%d', errors = 'coerce')
        df["DaysDiff"] = refDate - pd.to_datetime(df['BirthDate'], format='%d/%m/%Y')
        df["Age"] = df["DaysDiff"].dt.days.astype("Int16") // 365
        df.drop('DaysDiff', axis=1, inplace=True)
        return df

    def calculate_salarybucket(self, df: pd.DataFrame) -> pd.DataFrame:    
        df['SalaryBucket'] = np.where(df['Salary'] < 50000, 'A', '')
        df['SalaryBucket'] = np.where(df['Salary'] >= 100000, 'C', 'B')
        return df
    
if __name__ == '__main__':
    filepath_source = 'data/member-data.csv'
    referenceDate = '20240301'
    file_object = FileDataClass(filepath_source)
    df_file = file_object.create_df()
    df_file = file_object.process_date(df_file)
    df_file = file_object.process_string(df_file)
    df_file = file_object.calculate_salarybucket(df_file)
    df_file = file_object.process_number(df_file)
    df_file = file_object.calculate_age(df_file, referenceDate)
    df_file = df_file.drop(columns=['FirstName','LastName'], axis=1)
    print(df_file.head(10))

    df_file.to_json('output/enriched_data.json', orient='records', lines=True)