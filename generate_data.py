import numpy as np
import os

# Sample data creation (replace with actual data if available)
X_data = np.random.rand(1000, 10)  # 1000 samples, 10 features each
y_data = np.random.randint(0, 3, size=(1000,))  # 1000 samples, 3 classes (0, 1, 2)

# Define the folder path
folder_path = 'D:/as/data/'

# Create folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Save the data
np.save(os.path.join(folder_path, 'X_data.npy'), X_data)
np.save(os.path.join(folder_path, 'y_data.npy'), y_data)

print(f"Data saved successfully in {folder_path}")
