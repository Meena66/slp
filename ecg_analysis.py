# health_data/ecg_analysis.py
import numpy as np
import scipy.signal as signal

class ECGAnalysis:
    def __init__(self, ecg_data, fs=250):
        """
        Initialize ECG analysis with ECG data and sampling frequency.
        :param ecg_data: array-like, raw ECG signal data
        :param fs: int, sampling frequency in Hz (default 250Hz)
        """
        self.ecg_data = ecg_data
        self.fs = fs

    def bandpass_filter(self, lowcut=0.5, highcut=50):
        """
        Apply a bandpass filter to the ECG signal to remove noise.
        :param lowcut: float, low cutoff frequency in Hz
        :param highcut: float, high cutoff frequency in Hz
        :return: filtered ECG signal
        """
        nyquist = 0.5 * self.fs
        low = lowcut / nyquist
        high = highcut / nyquist
        b, a = signal.butter(1, [low, high], btype='band')
        filtered_ecg = signal.lfilter(b, a, self.ecg_data)
        return filtered_ecg

    def detect_r_peaks(self, filtered_ecg, threshold=0.6):
        """
        Detect R-peaks in the ECG signal using a simple thresholding method.
        :param filtered_ecg: array-like, filtered ECG signal
        :param threshold: float, detection threshold for R-peaks
        :return: array of R-peak indices
        """
        peaks, _ = signal.find_peaks(filtered_ecg, height=threshold, distance=self.fs/2)
        return peaks

    def calculate_heart_rate(self, r_peaks):
        """
        Calculate the heart rate (beats per minute) from R-peak intervals.
        :param r_peaks: array-like, indices of R-peaks
        :return: heart rate in beats per minute (bpm)
        """
        rr_intervals = np.diff(r_peaks) / self.fs  # Convert sample differences to time in seconds
        heart_rate = 60.0 / np.mean(rr_intervals)  # Beats per minute
        return heart_rate

    def detect_afib(self, rr_intervals):
        """
        Detect atrial fibrillation based on the irregularity of RR intervals.
        :param rr_intervals: array-like, RR intervals (time between R-peaks)
        :return: bool, True if AFib detected, False otherwise
        """
        rr_std = np.std(rr_intervals)
        return rr_std > 0.1  # A simple heuristic: large RR interval variance may indicate AFib

    def analyze(self):
        """
        Main method to analyze the ECG signal.
        :return: dict containing heart rate, AFib detection result, and R-peak positions
        """
        filtered_ecg = self.bandpass_filter()
        r_peaks = self.detect_r_peaks(filtered_ecg)
        rr_intervals = np.diff(r_peaks) / self.fs
        heart_rate = self.calculate_heart_rate(r_peaks)
        afib_detected = self.detect_afib(rr_intervals)

        return {
            'heart_rate': heart_rate,
            'afib_detected': afib_detected,
            'r_peaks': r_peaks
        }
