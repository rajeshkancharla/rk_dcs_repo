# ETL Assignment

**Requirements**

Building an ETL Pipeline that can extracts the data from a flat file, perform transformations on the data and loads the data into JSON file and MongoDB Collection

**Extraction**

The Extraction Module is built using Python's native Pandas library. As it's a CSV file the respective function is used. 
The same can be achieved using PySpark in case of a large dataset on a multi node cluster.


**Transformation**

The transformations of the required fields has been done using Pandas libraries.
In a multi node cluster, the same would be done through Pyspark transformations and actions instead of Pandas libraries.


**Load**

The final pandas dataframe is saved as a JSON file in the output folder.
Also the data is written into MongoDB Database running in localhost.
