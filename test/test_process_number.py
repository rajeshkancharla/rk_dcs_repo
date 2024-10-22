import os
import sys
import pandas as pd
import unittest

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from src.process_file import FileDataClass

class TestProcessNumber(unittest.TestCase):

    def test_process_number(self):
        filepath_source = 'data/sample.csv'        
        file_object = FileDataClass(filepath_source)
        df_file = file_object.create_df()
        df_new = file_object.process_number(df_file)
        self.assertEqual(df_new['Salary'][0], '$330,949.2034')


if __name__ == '__main__':
    unittest.main()