import os
import sys
import pandas as pd
import unittest

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from src.process_file import FileDataClass

class TestCalculateAge(unittest.TestCase):

    def test_calculate_age(self):
        referenceDate = '20240301'
        filepath_source = 'data/sample.csv'        
        file_object = FileDataClass(filepath_source)
        df_file = file_object.create_df()
        df_file = file_object.process_date(df_file)
        df_new = file_object.calculate_age(df_file, referenceDate=referenceDate)
        print('Derived Output  : ' + str(df_new['Age'][0]))
        print('Expected Output : ' + '34')
        self.assertEqual(df_new['Age'][0], 34)


if __name__ == '__main__':
    print("Unit Test for age calculation")
    unittest.main()