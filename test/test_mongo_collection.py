import os
import sys
import pandas as pd
import unittest
from pymongo import MongoClient

class TestMongoData(unittest.TestCase):

    def test_mongodata(self):

        client = MongoClient("mongodb://localhost:27017/")
        db = client['local']
        collection = db['MemberDataCollection']

        query = collection.aggregate([
            {
                '$match': {
                    'index': 0
                }
            }, {
                '$project': {
                    'Salary': 1, 
                    '_id': 0
                }
            }
        ])
        
        MongoClient.close(client)
        
        op = query.to_list()[0]["Salary"]  
        print('Derived Output  : ' + op)
        print('Expected Output : ' + '$330,949.2034')    
        self.assertEqual(op, '$330,949.2034')


if __name__ == '__main__':
    print("Unit Test for validating data in MongoDB")
    unittest.main()