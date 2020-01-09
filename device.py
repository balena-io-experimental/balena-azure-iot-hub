from busio import I2C
import adafruit_bme680
import time
import board
import os
import sys
import random

# Using the Python Device SDK for IoT Hub:
#   https://github.com/Azure/azure-iot-sdk-python
# The sample connects to a device-specific MQTT endpoint on your IoT Hub.
from azure.iot.device import IoTHubDeviceClient, Message

# The device connection string to authenticate the device with your IoT hub.
# Using the Azure CLI:
# az iot hub device-identity show-connection-string --hub-name {YourIoTHubName} --device-id MyNodeDevice --output table
if os.getenv('AZ_CONN_STR', 'none') == 'none':
    print ( "IoTHubClient: No connection string set, exiting..." )
    sys.exit(0)
else:
    CONNECTION_STRING = os.getenv('AZ_CONN_STR')

if os.getenv('AZ_USE_RANDOM', 'false') == 'false':
    
    # Create library object using our Bus I2C port
    i2c = I2C(board.SCL, board.SDA)
    bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

    # change this to match the location's pressure (hPa) at sea level
    bme680.sea_level_pressure = 1013.25
    # Define the JSON message to send to IoT Hub.
    TEMPERATURE = bme680.temperature
    HUMIDITY = bme680.humidity
else:
    TEMPERATURE = 20.0
    HUMIDITY = 60
    
MSG_TXT = '{{"temperature": {temperature},"humidity": {humidity}}}'

def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

def iothub_client_telemetry_sample_run():

    try:
        client = iothub_client_init()
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )

        while True:
            # Build the message.
            if os.getenv('AZ_USE_RANDOM', 'false') == 'false':
                temperature = bme680.temperature
                humidity = bme680.humidity
            else:
                temperature = TEMPERATURE + (random.random() * 15)
                humidity = HUMIDITY + (random.random() * 20)
                
            msg_txt_formatted = MSG_TXT.format(temperature=temperature, humidity=humidity)
            message = Message(msg_txt_formatted)

            # Add a custom application property to the message.
            # An IoT hub can filter on these properties without access to the message body.
            if temperature > 37:
              message.custom_properties["temperatureAlert"] = "true"
            else:
              message.custom_properties["temperatureAlert"] = "false"

            # Send the message.
            print( "Sending message: {}".format(message) )
            client.send_message(message)
            print ( "Message successfully sent" )
            time.sleep(5)

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

if __name__ == '__main__':
    print ( "IoT Hub balenaOS device..." )
    print ( "Starting to send data." )
    iothub_client_telemetry_sample_run()

