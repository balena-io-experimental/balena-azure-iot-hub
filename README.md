# balena-azure-iot-hub
Example using balena to push sensor data to Azure IoT Hub

Set environment variable AZ_CONN_STR to your Azure IoT Hub device connection string.
Looks for an I2C bme680 sensor to use for readings. If no sensor present, set environment variable AZ_USE_RANDOM to true to send random data instead.

To read back the data in real time from the hub see: https://docs.microsoft.com/en-us/azure/iot-hub/quickstart-send-telemetry-python#read-the-telemetry-from-your-hub
