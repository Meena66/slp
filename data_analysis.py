import numpy as np

# Function to analyze heart rate data (e.g., to check for abnormal levels)
def analyze_heart_rate(heart_rate_data):
    # Calculate the mean and standard deviation of heart rate
    mean_hr = np.mean(heart_rate_data)
    std_hr = np.std(heart_rate_data)
    
    # Check if the heart rate is within normal range (e.g., 60-100 bpm)
    abnormal_heart_rate = [hr for hr in heart_rate_data if hr < 60 or hr > 100]
    
    return mean_hr, std_hr, abnormal_heart_rate

# Function to analyze SpO2 data (e.g., detect low oxygen levels)
def analyze_spo2(spo2_data):
    # Calculate the mean and standard deviation of SpO2 levels
    mean_spo2 = np.mean(spo2_data)
    std_spo2 = np.std(spo2_data)
    
    # Identify SpO2 values that are too low (< 90%)
    low_spo2 = [spo2 for spo2 in spo2_data if spo2 < 90]
    
    return mean_spo2, std_spo2, low_spo2

# Function to perform a combined health analysis
def analyze_health_data(heart_rate_data, spo2_data):
    hr_mean, hr_std, hr_abnormal = analyze_heart_rate(heart_rate_data)
    spo2_mean, spo2_std, spo2_low = analyze_spo2(spo2_data)
    
    # Compile the results into a summary
    health_summary = {
        "heart_rate": {"mean": hr_mean, "std_dev": hr_std, "abnormal_values": hr_abnormal},
        "spo2": {"mean": spo2_mean, "std_dev": spo2_std, "low_spo2_values": spo2_low}
    }
    
    return health_summary
