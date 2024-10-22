import os
import sys
import pandas as pd
import unittest

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from src.process_file import FileDataClass

class TestCalculateSalaryBucket(unittest.TestCase):

    def test_calculate_salarybucket(self):
        filepath_source = 'data/sample.csv'        
        file_object = FileDataClass(filepath_source)
        df_file = file_object.create_df()
        df_new = file_object.calculate_salarybucket(df_file)
        print('Derived Output  : ' + str(df_new['SalaryBucket'][0]))
        print('Expected Output : ' + 'C')
        self.assertEqual(df_new['SalaryBucket'][0], 'C')


if __name__ == '__main__':
    print("Unit Test for salary bucket")
    unittest.main()