# ETL Assignment

**Requirements**

Building an ETL Pipeline that can extracts the data from a flat file, perform transformations on the data and loads the data into JSON file and MongoDB Collection

==================================================================

**Extraction**

The Extraction Module is built using Python's native Pandas library. As it's a CSV file the respective function is used. 
The same can be achieved using PySpark in case of a large dataset on a multi node cluster.


**Transformation**

The transformations of the required fields has been done using Pandas libraries.
In a multi node cluster, the same would be done through Pyspark transformations and actions instead of Pandas libraries.


**Load**

The final pandas dataframe is saved as a JSON file in the output folder.
Also the data is written into MongoDB Database running in localhost.

==================================================================

**Libraries Used**

As specified in the requirements for the assignment, only core packages/libraries listed below are used
1. os
2. sys
3. pandas
4. numpy
5. pymongo
6. unittest

==================================================================

**Test Driven Development - Automated Testing**

The python library unittest is used for the purpose of automated testing. While it is possible to granularize test case, one sample row from the source file is considered as sample.csv and all test cases were built around it. The assertions are used to validate the output against the expected results. Please find below the automated unit test results

<img width="1000" alt="image" src="https://github.com/user-attachments/assets/60e03f64-7fc5-4478-994a-3a3f130a7ffb">

<img width="1000" alt="image" src="https://github.com/user-attachments/assets/4dcd334a-af7e-41ff-b548-1702dab2b4b4">

<img width="1000" alt="image" src="https://github.com/user-attachments/assets/5109191a-0cef-43b4-89f8-01286aed2226">

<img width="1000" alt="image" src="https://github.com/user-attachments/assets/0499b930-bbfa-48d0-85f9-51df678f10c1">

<img width="1000" alt="image" src="https://github.com/user-attachments/assets/ef3a2967-49e3-4927-a08c-e08c5c9dab8b">


==================================================================

**Writing to MongoDB**

As the project is done in local machine, a local host of MongoDB is used to host the database and underlying collections

<img width="1000" alt="image" src="https://github.com/user-attachments/assets/1e93f889-cdac-4d16-b3f7-7834652e1fe9">

Test Case for MongoDB

<img width="1000" alt="image" src="https://github.com/user-attachments/assets/dd6891bb-708d-447a-98e0-64a75331b0cd">

==================================================================

**Running End to End ETL**

There is a main file called run_etl.py which calls all the modules and runs them in sequence. The output is as shown below

<img width="1000" alt="image" src="https://github.com/user-attachments/assets/bbbb2db8-62e5-4c01-94ee-1c1df3c64dd9">

==================================================================
