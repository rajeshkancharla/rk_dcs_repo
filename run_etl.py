from pymongo import MongoClient
from src.process_file import FileDataClass

    
def main():
    """
    This is the main function which calls each of the individual functions
    """

    # defining the global variables
    filepath_source = 'data/member-data.csv'
    referenceDate = '20240301'

    # instantiating the class to an object
    file_object = FileDataClass(filepath_source)

    # create data frame from the file
    df_file = file_object.create_df()
    print("   1. EXTRACTION     : Created the Dataframe from the file")

    # process the birth date field from integer to DD/MM/YYYY format
    df_file = file_object.process_date(df_file)
    print("   2. TRANSFORMATION : Date Processing Completed")

    # process the first and last name fields, trim spaces and create full name field
    df_file = file_object.process_string(df_file)
    print("   3. TRANSFORMATION : String Processing Completed")

    # create a new column called salary bucket which can be A / B / C
    df_file = file_object.calculate_salarybucket(df_file)
    print("   4. TRANSFORMATION : Creation of SalaryBucket field Completed")

    # process the salary value from a floating point value to a currency value with $ symbol, commas and decimals
    df_file = file_object.process_number(df_file)
    print("   5. TRANSFORMATION : Number to Currency Processing Completed")

    # create a new column called age which stores the age of the member
    df_file = file_object.calculate_age(df_file, referenceDate)
    print("   6. TRANSFORMATION : Creation of Age field Completed")

    # drop the first and last name columns
    df_file = df_file.drop(columns=['FirstName','LastName'], axis=1)
    print("   7. TRANSFORMATION : Dropping of unwanted fields Completed")

    # save the data to a JSON file and store it in folder
    df_file.to_json('output/enriched_data.json', orient='records', lines=True)
    print("   8. LOAD           : Saving the file as JSON Completed")

    # establish connection to MongoDB and instantiate the db and collection variables
    client = MongoClient("mongodb://localhost:27017/")
    db = client['local']
    collection = db['MemberDataCollection']

    # prepare the pandas dataframe to a dictionary before writing into MongoDB collection
    df_file.reset_index(inplace=True)
    data_dict = df_file.to_dict("records")

    # insert into MongoDB collection
    collection.insert_many(data_dict)
    print("   9. LOAD           : Writing to MongoDB Collection Completed")

    # close the connection to MongoDB
    MongoClient.close(client)


if __name__ == '__main__':
    print("Start of E T L Processing")
    main()
    print("End of E T L Processing")