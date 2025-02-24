from bleak import BleakClient
import asyncio

# UUIDs for the heart rate and SpO2 characteristics (example)
HEART_RATE_UUID = "00002a37-0000-1000-8000-00805f9b34fb"
SPO2_UUID = "00002a5f-0000-1000-8000-00805f9b34fb"

# Function to connect to the smartwatch and retrieve health data
async def get_health_data(device_address):
    async with BleakClient(device_address) as client:
        # Check if connected
        if not client.is_connected:
            raise Exception("Unable to connect to device")
        
        # Read heart rate data
        heart_rate = await client.read_gatt_char(HEART_RATE_UUID)
        
        # Read SpO2 data
        spo2 = await client.read_gatt_char(SPO2_UUID)
        
        # Decode byte data into human-readable format
        heart_rate_value = int.from_bytes(heart_rate, byteorder='little')
        spo2_value = int.from_bytes(spo2, byteorder='little')
        
        return heart_rate_value, spo2_value

# Function to start the Bluetooth sync process
def sync_health_data(device_address):
    loop = asyncio.get_event_loop()
    heart_rate, spo2 = loop.run_until_complete(get_health_data(device_address))
    return heart_rate, spo2

