import bme680
import sys

sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

# These oversampling settings can be tweaked to
# change the balance between accuracy and noise in
# the data.

sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)
i = 0
while i < 20:
    i+=1
    sensor.get_sensor_data()

if sensor.get_sensor_data():
   print('{0:0.1f} | {1:0.1f}'.format(sensor.data.temperature, sensor.data.humidity))
