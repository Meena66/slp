import unittest
import numpy as np
from models.tensorflow_model import predict_sleep_apnea

class TestModels(unittest.TestCase):
    # Test prediction for sleep apnea detection
    def test_predict_sleep_apnea(self):
        test_data = np.array([75, 95, 0.3])  # Example data (HR, SpO2, ECG)
        prediction = predict_sleep_apnea(test_data)
        self.assertIn(prediction, ["Obstructive", "Central", "Complex", "Normal"])

if __name__ == '__main__':
    unittest.main()
