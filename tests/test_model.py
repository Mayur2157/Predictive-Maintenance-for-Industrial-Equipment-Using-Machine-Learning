import os
import sys
import unittest
import pandas as pd
from unittest.mock import patch
from sklearn.ensemble import RandomForestClassifier
import tempfile
import shutil

# Add the parent directory of src to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.model import train_model, predict

class TestModel(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for model saving
        self.test_dir = tempfile.mkdtemp()
        self.model_path = os.path.join(self.test_dir, 'random_forest_model.pkl')

        # Sample data for training
        data = {
            'Temperature (°C)': [25.0, 30.0, 27.0],
            'Vibration (mm/s)': [0.5, 0.7, 0.6],
            'Pressure (Pa)': [101325, 101400, 101350],
            'RPM': [1500, 1600, 1550],
            'Temp_Change': [0.1, 0.2, 0.15],
            'Vib_Change': [0.02, 0.03, 0.025],
            'Maintenance Required': [0, 1, 0]
        }
        self.df = pd.DataFrame(data)

        # Patch the train_model function to use the temporary directory
        with patch('src.model.joblib.dump') as mock_dump:
            self.model = train_model(self.df[['Temperature (°C)', 'Vibration (mm/s)', 'Pressure (Pa)', 'RPM', 'Temp_Change', 'Vib_Change']],
                                     self.df['Maintenance Required'])
            self.mock_dump = mock_dump

    def tearDown(self):
        # Clean up temporary directory
        shutil.rmtree(self.test_dir)

    def test_model_training(self):
        # Test if the model is trained correctly
        self.assertIsInstance(self.model, RandomForestClassifier)
        self.assertGreater(len(self.model.estimators_), 0)

    def test_model_prediction(self):
        # Test model prediction
        test_data = pd.DataFrame({
            'Temperature (°C)': [28.0],
            'Vibration (mm/s)': [0.65],
            'Pressure (Pa)': [101370],
            'RPM': [1575],
            'Temp_Change': [0.18],
            'Vib_Change': [0.027]
        })
        prediction = predict(self.model, test_data)
        self.assertIn(prediction[0], [0, 1])

if __name__ == '__main__':
    unittest.main()
