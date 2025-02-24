import unittest
from health_data.bluetooth_sync import sync_data

class TestBluetooth(unittest.TestCase):
    # Test Bluetooth data synchronization
    def test_sync_data(self):
        result = sync_data()  # Assuming sync_data returns a dictionary of sensor data
        self.assertTrue("heart_rate" in result)
        self.assertTrue("spo2" in result)

if __name__ == '__main__':
    unittest.main()
