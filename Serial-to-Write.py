import pigpio
import serial
from time import sleep
import datetime
import DHT22 

Pi = pigpio.pi()

Ser = serial.Serial()
Ser.baudrate = 9600
Ser.port = '/dev/ttyUSB0'
Ser.open()

Sensordata = DHT22.sensor(pi, 4)

while True:
	
	Sensordata.trigger() #started getting data from device.
	sleep(60) #seconds.

	x = '{:0.0f}'.format(Sensordata.temperature() / 1.)
	y = '{:0.0f}'.format(Sensordata.humidity() / 1.)
	
	time = datetime.datetime.now().strftime("%H:%M")
	
	print (x + ',' + y + ' : ' + time) # For seeing values and time on terminal.
	
	x1 = x + ',' # Sending data values in an order so we can easily use and processing data on Rx device.
	y1 = y
	
	Ser.write(x1.encode()) # Encoding to bytes. 
	Ser.write(y1.encode()) # Encoding to bytes.

Sensordata.cancel()
Pi.stop()
Ser.close()
