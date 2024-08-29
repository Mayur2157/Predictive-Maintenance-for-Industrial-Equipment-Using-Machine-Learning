import unittest
import pandas as pd
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_preprocessing import preprocess_data

class TestDataPreprocessing(unittest.TestCase):

    def setUp(self):
        # Sample data to use in tests
        data = {
            'Timestamp': ['2024-01-01 00:00:00', '2024-01-01 01:00:00'],
            'Temperature (°C)': [25.0, 30.0],
            'Vibration (mm/s)': [0.5, 0.7],
            'Pressure (Pa)': [101325, 101400],
            'RPM': [1500, 1600],
            'Maintenance Required': [0, 1]
        }
        self.df = pd.DataFrame(data)
    
    def test_preprocess_data(self):
        processed_df = preprocess_data(self.df)

        # Check if 'Temp_Change' and 'Vib_Change' columns are present
        self.assertIn('Temp_Change', processed_df.columns)
        self.assertIn('Vib_Change', processed_df.columns)

        # Ensure there are no NaN values after preprocessing
        self.assertFalse(processed_df.isnull().values.any())

    def test_empty_dataframe(self):
        # Test with an empty dataframe
        empty_df = pd.DataFrame()
        processed_df = preprocess_data(empty_df)
        self.assertTrue(processed_df.empty)

if __name__ == '__main__':
    unittest.main()
