# balena-azure-iot-hub
Example using balena to push sensor data to Azure IoT Hub

Step 1: Create an IoT Hub using the Azure portal by following [these instructions](https://docs.microsoft.com/en-us/azure/iot-dps/quick-setup-auto-provision). At the end of this step, you should have a Resource Group Name (existing or new,) IoT Hub Name and a Device Provisioning Service name.  The IoT hub should be linked to your Device Provisioning Service.

Step 2: Enroll X.509 devices to the Device Provisioning Service using Python with [these instructions](https://docs.microsoft.com/en-us/azure/iot-dps/quick-enroll-device-x509-python).

Set environment variable AZ_CONN_STR to your Azure IoT Hub device connection string.
Looks for an I2C bme680 sensor to use for readings. If no sensor present, set environment variable AZ_USE_RANDOM to true to send random data instead.

To read back the data in real time from the hub see: https://docs.microsoft.com/en-us/azure/iot-hub/quickstart-send-telemetry-python#read-the-telemetry-from-your-hub
