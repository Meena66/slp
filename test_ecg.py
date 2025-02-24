# tests/test_ecg.py

import unittest
import numpy as np
from health_data.ecg_analysis import ECGAnalysis

class TestECGAnalysis(unittest.TestCase):

    def test_heart_rate_calculation(self):
        # Simulated R-peak data (indices) at a heart rate of 60 bpm, 250 Hz sampling frequency
        simulated_r_peaks = np.array([250, 500, 750, 1000, 1250, 1500])
        ecg_analyzer = ECGAnalysis(ecg_data=np.zeros(2000), fs=250)
        heart_rate = ecg_analyzer.calculate_heart_rate(simulated_r_peaks)
        self.assertAlmostEqual(heart_rate, 60, delta=1)

    def test_afib_detection(self):
        # Simulated RR intervals for AFib detection
        rr_intervals_regular = np.array([1, 1, 1, 1])  # Regular intervals
        rr_intervals_irregular = np.array([1, 0.8, 1.2, 0.9])  # Irregular intervals (AFib)

        ecg_analyzer = ECGAnalysis(ecg_data=np.zeros(2000), fs=250)

        self.assertFalse(ecg_analyzer.detect_afib(rr_intervals_regular))
        self.assertTrue(ecg_analyzer.detect_afib(rr_intervals_irregular))

if __name__ == '__main__':
    unittest.main()
