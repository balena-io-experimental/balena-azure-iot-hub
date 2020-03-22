# balena-azure-iot-hub
Example using balena to push sensor data to Azure IoT Hub

Hardware: This example is designed to use on a Raspberry Pi with an I2C BME680 sensor connected. If no sensor is present on your device, set the balena environment variable `AZ_USE_RANDOM` to true to send random data instead.

Step 1: Create an IoT Hub using the Azure portal by following [these instructions](https://docs.microsoft.com/en-us/azure/iot-dps/quick-setup-auto-provision). For this example, you do not need to create a Device Provisioning Service.

Step 2: In your Azure Portal IoT hub navigation menu, open "IoT Devices", then select "New" to add a device in your IoT hub. (Select "Symmetric key" and check "Auto-generate keys")

Step 3: After the device is created, open the device in the Azure Portal from the list in the IoT devices pane. Copy the Primary Connection String for use in a subsequent step below.

Step 4: Create a balena application from the balenaCloud dashboard and add a device to download an image. Burn the image onto the appropriate media for your device (SD card/micro SD card)

Step 4: Clone this repository and use the balena CLI to push this code to your device. Once the device appears on the dashboard, set a device variable named `AZ_CONN_STR` using the value copied from the Azure portal in step 3 above.

Your device will restart and it should start sending data to the hub. To read back the data in real time from the hub see: https://docs.microsoft.com/en-us/azure/iot-hub/quickstart-send-telemetry-python#read-the-telemetry-from-your-hub
